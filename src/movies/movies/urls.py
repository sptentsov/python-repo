from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',)


urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('movieproj.views',
    url(r'^lists/$', 'lists'),
	url(r'^reg/$', 'reg'),
    url(r'^login/$', 'mylogin'),
    url(r'^logout/$', 'mylogout'),
	url(r'^createacc/$', 'createacc'),
	url(r'^$', 'main'),
)
