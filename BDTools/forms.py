# Copyright (C) 2008 Instituto Nokia de Tecnologia. All rights reserved.
# Contact: Ian Lawrence root@ianlawrence.info
#
# This software, including documentation, is protected by copyright
# controlled by Instituto Nokia de Tecnologia. All rights are reserved.
# Copying, including reproducing, storing, adapting or translating, any
# or all of this material requires the prior written consent of
# Instituto Nokia de Tecnologia. This material also contains
# confidential information which may not be disclosed to others without
# the prior written consent of Instituto Nokia de Tecnologia.
#




from django import forms
from django.http import HttpResponseRedirect
from django.contrib.formtools.wizard import FormWizard
from models import Spreadsheet, BusinessCase
from django.shortcuts import get_object_or_404



class Spread1(forms.Form):
    CHOICES = [(x, x) for x in ("Yes", "No")]
    value_proposal = forms.ChoiceField(choices=CHOICES, help_text="Adds value to INdT and/or Nokia customers or consumers and/or brings about benefits to Nokia, INdT, partners or government?")
    conflict = forms.ChoiceField(choices=CHOICES, help_text="Is the project in conflict with INdT customers market and product policies?")
    innovation = forms.ChoiceField(choices=CHOICES, help_text="Does the project create new, applicable and appropriable knowledge or/and does the project combine knowledge in an innovative manner?")


    def clean(self):
        cleaned_data = self.cleaned_data
        value_proposal = cleaned_data.get("value_proposal")
        conflict = cleaned_data.get("conflict")
        innovation = cleaned_data.get("innovation")

        if value_proposal not in "Yes":
                raise forms.ValidationError("The project must add value to INdT or bring about benefits to Nokia, INdT, partners or government. The project fails at this Stage Gate")
        if conflict not in "No":
                raise forms.ValidationError("The project conflicts with INdT customers market and product policies. The project fails at this Stage Gate")
        if innovation not in "Yes":
                raise forms.ValidationError("The project does not create new, applicable and appropriable knowledge. The project fails at this Stage Gate")

        # Always return the full collection of cleaned data.
        return cleaned_data

class Spread2(forms.Form):
    CHOICES = (
        (1, 'Poor'),
        (2, 'Regular'),
        (3, 'Good'),
        (4, 'Very Good'),
    )
    CHOICES1 = (
        (1, 'No appropriability'),
        (2, 'Low level of appropriability'),
        (3, 'Moderate'),
        (4, 'Patentable by patent, difficult to be broken'),
    )
    CHOICES2 = (
        (1.2, 'No technological risk'),
        (1.4, 'Low level of technological risk'),
        (1.6, 'Moderate technological risk'),
        (1.8, 'High technological risk'),
    )
    CHOICES3 = (
       (1, 'Costs very low compared to projects returns'),
       (2, 'Costs lower than the projects returns'),
       (3, 'Costs aligned to the projects returns'),
       (4, 'Costs may be too high when compared to the project returns'),
    )
    CHOICES4 = (
       (1, 'Narrow'),
       (2, 'Moderate'),
       (3, 'Wide'),
    )
    CHOICES5 = (
       (1, 'Moderately'),
       (2, 'Substantially'),
    )
    CHOICES6 = (
      (1, 'Regional'),
      (2, 'Brazil'),
      (3, 'LA'),
      (4, 'Worldwide'),
    )
    CHOICES7 = (
      (1, 'Reinforces current competencies'),
      (2, 'Closes competency vis-a-vis competitors'),
      (3, 'Build new core competencies'),
    )
    quality = forms.ChoiceField(choices=CHOICES, help_text="What is the quality of information presented.?")
    strategic = forms.ChoiceField(choices=CHOICES, help_text="How much does this project align with INdT strategy?")
    competency = forms.ChoiceField(choices=CHOICES7,help_text="What is the probability that the project will build competencies?")
    markets = forms.ChoiceField(choices=CHOICES6, help_text="The project opens new, significant markets for INdT or Nokia (What is the potential for market and revenue creation?)")
    leverage = forms.ChoiceField(choices=CHOICES5,help_text="What is the project's capacity to leverage INdT/Nokia's competitive position (Impact on competition)")
    span = forms.ChoiceField(choices=CHOICES4,help_text="If the project is approved what is the span of possible applications that the resulting product might be applied to?")
    IPR = forms.ChoiceField(label='IPR',choices=CHOICES1,help_text="Are there any IPR implications?")
    technological_feasibility = forms.ChoiceField(choices=CHOICES, help_text="What is the technological feasibility of the project?")
    cost = forms.ChoiceField(choices=CHOICES3,help_text="Assuming the project is implemented the set up costs of it are likely to be")
    technological_risk  = forms.ChoiceField(choices=CHOICES2,help_text="What are the technological risks")

class SpreadWizard(FormWizard):
    def __init__(self, *args, **kwargs):
        super(SpreadWizard, self).__init__(*args, **kwargs)
        

    def done(self, request, form_list):
        # Save to the database and run the algorithm on it    
        form_data = {}
        for form in form_list:
          form_data.update(form.cleaned_data)
          # include the fields missing in the database model
          form_data.update({'business_case_id': request.POST['business_case_id']})
          form_data.update({'user': request.user})
        new_spreadsheet = Spreadsheet.objects.create(**form_data)
        return HttpResponseRedirect('/calculate/%s'%new_spreadsheet.id)
               

    def parse_params(self, request, *args, **kwargs):
        # pass over the extra info about the Business Case
        browsing = get_object_or_404(BusinessCase, id=kwargs['browsing_id'])
        self.extra_context['browsing'] = browsing




