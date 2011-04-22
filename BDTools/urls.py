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

from Innovation.BDTools.forms import Spread1, Spread2, SpreadWizard

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
     (r'^$', 'Innovation.BDTools.views.index'),
     (r'^browse/$', 'Innovation.BDTools.views.browse'),
     (r'^browse/(?P<project_id>\d+)/$', 'Innovation.BDTools.views.browsing'),
     (r'^add/$', 'Innovation.BDTools.views.add'),
     (r'^thanks/(?P<project_id>\d+)/$', 'Innovation.BDTools.views.thanks'),
     (r'^calculate/(?P<new_spreadsheet_id>\d+)/$', 'Innovation.BDTools.views.calculate'),
     (r'^spreadsheet/(?P<browsing_id>\d+)/$', SpreadWizard([Spread1, Spread2])),
     (r'^rank/$', 'Innovation.BDTools.views.rank'),
     (r'^assessed/$', 'Innovation.BDTools.views.assessed'),

     # about, credits etc
     (r'^about/$', 'Innovation.BDTools.views.about'),
     (r'^credits/$', 'Innovation.BDTools.views.credits'),
     (r'^terms/$', 'Innovation.BDTools.views.terms'),
     # admin
     (r'^admin/', include(admin.site.urls)),

     # serve media for runserver
     (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/home/ian/Web/django_projects/Innovation/core/media'}),
)

# serve media for runserver
if settings.LOCAL_DEV:
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/home/ian/Web/django_projects/Innovation/core/media'}),
