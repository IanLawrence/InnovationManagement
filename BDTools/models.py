# Copyright (C) 2009 Instituto Nokia de Tecnologia. All rights reserved.
# Contact: Ian Lawrence ian.lawrence@openbossa.org
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
# Django Framework models- database classes ian.lawrence@openbossa.org
#
#
#===========================================================================

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



       
           

class BusinessCase(models.Model):
    CHOICES1 = (
        (u'New to the world', u'New to the world'),
        (u'New to the LTA market', u'New to the LTA market'),
        (u'Useful to close INdT or Nokia technological gap', u'Useful to close INdT or Nokia technological gap'),
    )
    CHOICES2 = (
        (u'Reinforces current competencies', u'Reinforces current competencies'),
        (u'Closes competency gap vis-a-vis competitors', u'Closes competency gap vis-a-vis competitors'),
        (u'Builds new core competency', u'Builds new core competency'),
    )
    CHOICES3 = (
        (u'Yes, in Brazil', u'Yes, in Brazil'),
        (u'Yes, in LTA', u'Yes, in LTA'),
        (u'Yes, worldwide', u'Yes, worldwide'),
    )
    CHOICES4 = (
        (u'Yes, moderately', u'Yes, moderately'),
        (u'Yes, substantially', u'Yes, substantially'),
    )
    CHOICES5 = (
        (u'Narrow', u'Narrow'),
        (u'Moderate', u'Moderate'),
        (u'Wide', u'Wide'),
    )
    CHOICES6 = (
        (u'Low level of appropriability', u'Low level of appropriability'),
        (u'Moderate', u'Moderate'),
        (u'Protectable by patent difficult to be broken', u'Protectable by patent difficult to be broken'),
    )
    submitter = models.CharField(help_text="Your Name", max_length=100)
    project_name = models.CharField(help_text="Proposed Project Name", max_length=100)
    project_description = models.TextField(help_text="Project Description")
    value_proposal_and_objective = models.TextField(help_text="Is value added to INdT or Nokia's consumers?")
    benefits = models.TextField(help_text="What are the benefits to Nokia, INdT, Partners or Governments?")
    problem = models.TextField(help_text="Describe the problems the project addresses and/or the general field of technology being explored?")
    deliverables = models.TextField(help_text="What are the final deliverables and what is innovative in your project?")
    innovative = models.CharField(choices=CHOICES1, help_text="What are the knowledge-creation and knowledge-combination aspects of the project.", max_length=300)
    application_strategic_contribution = models.TextField(help_text="Justify the strategy alignment of the application. Indicate key strategy elements to which the project contributes")
    competence_building = models.CharField(choices=CHOICES2, help_text="What is the proposed projects contribution to competency building?", max_length=300)
    market_attractiveness = models.CharField(choices=CHOICES3, help_text="Does the proposed projects resulting technology or solution open new, significant markets for INdT or Nokia's consumers?",max_length=300)
    competitiveness = models.CharField(choices=CHOICES4, help_text="Does the proposed projects resulting technology or solution have potential to leverage INdT/Nokia's competitive position?",max_length=300)
    technology_attractiveness = models.CharField(choices=CHOICES5, help_text="The resulting solution or technology has a span of possible applications which is...?",max_length=300)
    appropriability = models.CharField(choices=CHOICES6, help_text="Is the technology/solution appropriate for INdT?. Why?", max_length=300)
    technological_feasibility = models.TextField(help_text="What are the biggest project blockers from a technological perspective?")
    cost = models.TextField(help_text="Please estimate the resources needed  (in a high level overview) for the development of your idea (Things like headcount, equipment, hardware etc)")
    experts_recommendation = models.TextField(help_text="The Names of the people involved in this project. Their innovation area, technology speciality or stream manager")
    
    class Admin:
       pass

    def __unicode__(self):
       return self.project_name
                                                                                                       


class Spreadsheet(models.Model):
    CHOICES1 = (
        (u'Yes', u'Yes'),
        (u'No', u'No'),
    )
    CHOICES2 = (
        (u'1 - Very Poor', u'1 - Very Poor'),
        (u'2 - Poor', u'2 - Poor'),
        (u'3 - Good', u'3 - Good'),
        (u'4 - Very Good', u'4 - Very Good'),
    )
    CHOICES3 = (
        (u'1 - Extremely Unlikely', u'1 - Extremely Unlikely'),
        (u'2 - Unlikely', u'2 - Unlikely'),
        (u'3 - Likely', u'3 - Likely'),
        (u'4 - Very Likely', u'4 - Very Likely'),
    )
    CHOICES4 = (
        (u'1 - Very Low', u'1 - Very Low'),
        (u'2 - Low', u'2 - Low'),
        (u'3 - High', u'3 - High'),
        (u'4 - Very High', u'4 - Very High'),
    )
    business_case = models.ForeignKey(BusinessCase)
    value_proposal = models.CharField(choices=CHOICES1,max_length=3,help_text="Adds value to INdT and/or Nokia customers or consumers and/or brings about benefits to Nokia, INdT, partners or government?")
    conflict= models.CharField(choices=CHOICES1,max_length=3,help_text="Is the project in conflict with INdT customers market and product policies?")
    innovation= models.CharField(choices=CHOICES1,max_length=3,help_text="Does the project create new, applicable and appropriable knowledge or/and does the project combine knowledge in an innovative manner?")
    irr = models.FloatField(editable=False,  blank=True, null=True)
    npv = models.FloatField(editable=False,  blank=True, null=True)
    ie = models.FloatField(editable=False,  blank=True, null=True)
    quality= models.FloatField(choices=CHOICES2, help_text="What is the quality of information presented.?")
    strategic= models.FloatField(choices=CHOICES2, help_text="How much does this project align with INdT strategy?")
    competency= models.FloatField(choices=CHOICES2,help_text="What is the probability that the project will build competencies?")
    markets= models.FloatField(choices=CHOICES2, help_text="The project opens new, significant markets for INdT's customers or Nokia's consumers (What is the potential for market and revenue creation?)")
    leverage= models.FloatField(choices=CHOICES2,help_text="What is the project's capacity to leverage INdT/Nokia's competitive position (Impact on competition)")
    span= models.FloatField(choices=CHOICES2,help_text="If the project is approved what is the span of possible applications that the resulting product might be applied to?")
    IPR= models.FloatField(choices=CHOICES3,help_text="Are there any IPR implications?")
    technological_feasibility= models.FloatField(choices=CHOICES2, help_text="What is the technological feasibility of the project?")
    cost = models.FloatField(choices=CHOICES4,help_text="Assuming the project is implemented the set up costs of it are likely to be")
    technological_risk= models.FloatField(choices=CHOICES4,help_text="What are the technological risks")
    date_created = models.DateTimeField()
    user = models.CharField(max_length=100)
    
    class Admin:
       pass
       
    def __unicode__(self):
       return self.business_case 

    # override the save method
    def save(self,*args, **kwargs):
      if self.date_created == None:
         self.date_created = datetime.now()
      super(Spreadsheet, self).save(*args, **kwargs)



     


