from django.conf.urls import patterns, include, url
from django.contrib import admin
import os

import settings

admin.autodiscover()






urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    #url(r'^cleanupfull/$', 'cleanup.views.CreateCleanupEvent', name='done'),
    #(r'^facebook/', include('django_facebook.urls')),
    #(r'^accounts/', include('django_facebook.auth_urls')), #Don't add this line if you use django registration or userena for registration and auth.
     #(r'^photologue/', include('photologue.urls')),
)
#Login 
urlpatterns += patterns('facebook.views',url(r'^$', 'login'),)
for app in settings.OUR_APPS:   
    urlpatterns += patterns('',url(r'^'+app+'/', include(app+'.urls',app_name=app)),)
    

if settings.DEBUG:
    
    urlpatterns += patterns('',
                        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root': settings.MEDIA_ROOT}),
                    )







