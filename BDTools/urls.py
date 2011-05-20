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

# Django imports
from django.conf.urls.defaults import *
from django.contrib import databrowse

from InnovationManagement.BDTools.forms import Spread1, Spread2, SpreadWizard

from django.conf import settings

# admin
from django.contrib import admin
admin.autodiscover()



#databrowse.site.register(Unit)

# urls for thememaker
urlpatterns = patterns('',
      #login related functionality
     (r'^accounts/login/$', 'django.contrib.auth.views.login'),
     (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
     
      # BD Tools 
     (r'^$', 'InnovationManagement.BDTools.views.index'),
     (r'^browse/$', 'InnovationManagement.BDTools.views.browse'),
     (r'^browse/(?P<project_id>\d+)/$', 'InnovationManagement.BDTools.views.browsing'),
     (r'^add/$', 'InnovationManagement.BDTools.views.add'),
     (r'^thanks/(?P<project_id>\d+)/$', 'InnovationManagement.BDTools.views.thanks'),
     (r'^calculate/(?P<new_spreadsheet_id>\d+)/$', 'InnovationManagement.BDTools.views.calculate'),
     (r'^spreadsheet/(?P<browsing_id>\d+)/$', SpreadWizard([Spread1, Spread2])),
     (r'^rank/$', 'InnovationManagement.BDTools.views.rank'),
     (r'^assessed/$', 'InnovationManagement.BDTools.views.assessed'),

     # about, credits etc
     (r'^about/$', 'Innovation.BDTools.views.about'),
     (r'^credits/$', 'Innovation.BDTools.views.credits'),
     (r'^terms/$', 'Innovation.BDTools.views.terms'),
     # admin
     (r'^admin/', include(admin.site.urls)),

     # uncomment to serve media for local server (Dhango 1.2)
     (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/home/ian/Dev/InnovationManagement/core/media'}),
)

