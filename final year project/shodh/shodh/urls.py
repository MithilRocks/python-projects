from django.conf.urls import include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'shodh.views.home', name='home'),
    # url(r'^shodh/', include('shodh.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search_form/','searchengine.views.search_form'),
    url(r'^search/','searchengine.views.search',name='hellosearch'),
	url(r'^thanks/','searchengine.views.thanks'),
	url(r'^display/(?P<id>\d)/$','searchengine.views.display',name='disp'),
	url(r'^autosuggest/', 'searchengine.views.autosuggest', name='auto_suggest'),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
]
