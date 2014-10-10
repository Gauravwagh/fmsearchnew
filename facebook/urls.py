from django.conf.urls import patterns, url

urlpatterns = patterns('facebook.views',
                        (r'^login/$','login' ),
                       (r'^home/$','home'),
                       (r'^search/$','artist_search'),
                       (r'^history/$','history'),
                       )