from django.conf.urls import patterns, include, url
from mako_controller import HtmlPageServer

urls = [ '',
  # homepage app
  (r'^$', HtmlPageServer('myhome') ),
  (r'^(?P<path>.*\.html)(?P<funcname>!.*?)?(?P<urlparams>/.*)?$', HtmlPageServer('myhome') ),  
]
# this is the variable Django really wants
urlpatterns = patterns(*urls)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sokratik.views.home', name='home'),
    # url(r'^sokratik/', include('sokratik.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
#)


