from django.conf.urls import patterns, include, url
from rango.views import current_datetime, index 
from twython_django_oauth.Tweet_view import test

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^tango_with_django_project/', include('tango_with_django_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	
	url(r'^rango/', include('rango.urls')), # ADD THIS NEW TUPLE!
	url(r'^twython/', include('twython_django_oauth.urls')),
	url(r'^time/$', current_datetime),
	url(r'^Maplecroft_twitter/$', test),
	# url(r'^Maplecroft_twitter/$', Tweet_view.test, name = "test"),
)
