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
#===========================================================================
#
# Django Framework views the work horse of the app root@ianlawrence.info
#
#===========================================================================


# django imports
from django.db.models import Max

# response and request
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseServerError,  HttpResponse
from django.template import Context, RequestContext 

#forms
from django.forms import ModelForm, Textarea

from django.forms.models import inlineformset_factory
import django.forms as forms


# templates
from django.template.loader import render_to_string


# registration
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.context_processors import csrf

# utils
from django.utils.html import escape

#urls
from django.core.urlresolvers import reverse


# Local imports
from Innovation.BDTools.models import   BusinessCase,  Spreadsheet
from Innovation.BDTools import juiz
 
# forms       
class BusinessCaseForm(ModelForm):
    class Meta:
        model = BusinessCase
        fields = ['project_name','submitter','project_description',  'value_proposal_and_objective', 'benefits',  'problem', 'deliverables',  'innovative', 
        'application_strategic_contribution', 'competence_building', 'market_attractiveness', 'competitiveness','technology_attractiveness','appropriability','technological_feasibility','cost','experts_recommendation']
        widgets = {
            'project_description': Textarea(attrs={'cols': 80, 'rows': 15}),
            'value_proposal_and_objective': Textarea(attrs={'cols': 80, 'rows': 15}),
            'benefits': Textarea(attrs={'cols': 80, 'rows': 15}),
            'problem': Textarea(attrs={'cols': 80, 'rows': 15}),
            'deliverables': Textarea(attrs={'cols': 80, 'rows': 15}),
            'application_strategic_contribution': Textarea(attrs={'cols': 80, 'rows': 15}),
            'technological_feasibility': Textarea(attrs={'cols': 80, 'rows': 15}),
            'cost': Textarea(attrs={'cols': 80, 'rows': 15}),
            'experts_recommendation': Textarea(attrs={'cols': 80, 'rows': 15}),
            
        }



# Main project views
def index(request):
    '''Returns the default start page of the site'''
    return render_to_response('BDTools/base_start.html',  context_instance=RequestContext(request))


@login_required
def browse(request):
    '''Browse all available projects in the system'''
    projects = BusinessCase.objects.all()
    return render_to_response('BDTools/base_browse.html',  {'projects': projects},  context_instance=RequestContext(request) )


def rank(request):
    '''Rank the projects in the system'''
    all_of_them = BusinessCase.objects.annotate(most_recent_spreadsheet=Max('spreadsheet__date_created')) 
    projects = Spreadsheet.objects.filter(date_created__in=[b.most_recent_spreadsheet for b in all_of_them]).order_by('-ie')
    return render_to_response('BDTools/base_rank.html',  {'projects': projects},  context_instance=RequestContext(request) )


@login_required
def browsing(request,  project_id):
     '''Browse all available projects in the system'''
     browsing = BusinessCase.objects.get(pk=project_id)
     return render_to_response('BDTools/base_browsing.html',  {'browsing': browsing},  context_instance=RequestContext(request) )


def add(request):
    '''Add a projects in the system'''
     # set the appropriate template
    form_template ='BDTools/base_add.html'
    if request.method == 'POST':
         # The forms submitted by the client.
        form =  BusinessCaseForm(request.POST)
        if form.is_valid():
            new_project = form.save()
            return HttpResponseRedirect('/thanks/%s'%new_project.id) # Redirect after POST
    else:
            # instantiate the form
        form =  BusinessCaseForm()
    return render_to_response(form_template,  {'form': form},  context_instance=RequestContext(request) )


def thanks(request,  project_id):
    form_template ='BDTools/base_thanks.html'
    project = get_object_or_404(BusinessCase, pk=project_id)
    return render_to_response(form_template,  {'project': project },  context_instance=RequestContext(request) )


@login_required
def calculate(request,  new_spreadsheet_id):
    form_template ='BDTools/base_analysis.html'
    proj = Spreadsheet.objects.select_related().get(pk=new_spreadsheet_id)
    try:
        rate, cashflows, resources = 0.09,[-(proj.cost), proj.quality,proj.strategic,proj.competency,proj.markets,proj.leverage,proj.span,proj.IPR,proj.technological_feasibility], proj.technological_risk
        proj.irr, proj.npv, proj.ie = juiz.investment_analysis(rate, [c for c in cashflows], resources)
        proj.save()
        #return render_to_response(form_template,  {'proj': proj },  context_instance=RequestContext(request) )
        return HttpResponseRedirect('/assessed/') # Redirect 
    except(KeyError):
        pass

@login_required
def assessed(request):
    form_template ='BDTools/base_assessed.html'
    return render_to_response(form_template,  context_instance=RequestContext(request) )

def about(request):
    '''Returns the about page of the site'''
    return render_to_response('BDTools/base_about.html',  context_instance=RequestContext(request))


def terms(request):
    '''Returns the terms page of the site'''
    return render_to_response('BDTools/base_terms.html',  context_instance=RequestContext(request))


def credits(request):
    '''Returns the credits page of the site'''
    return render_to_response('BDTools/base_credits.html',  context_instance=RequestContext(request))








   
    






    

        

    
