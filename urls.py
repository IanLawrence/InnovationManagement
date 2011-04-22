from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings


urlpatterns = patterns('',
    # Example:
    # (r'^PortfolioManagement/', include('PortfolioManagement.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
      (r'^admin/doc/', include('django.contrib.admindocs.urls')),
      
    #include the thememaker urls
      (r'^', include('Innovation.BDTools.urls')),
    

    # Uncomment the next line to enable the admin:
      (r'^admin/(.*)', admin.site.root),
)


