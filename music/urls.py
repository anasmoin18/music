from django.conf.urls import patterns, include, url
from django.contrib import admin
from gaana import views

urlpatterns = [
    url(r'^sign-up/$', views.sign_up, name='sign_up'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout_page'),
    url(r'^home/$', views.home, name='home'),
    url(r'^albums/$', views.albums, name='albums'),
    url(r'^artist/(?P<artist_id>\d+)/$', views.artist, name='artist'),
    url(r'^album/(?P<album_id>\d+)/$', views.album, name='album'),
    url(r'^playlists/$', views.playlists, name='playlists'),
    url(r'^playlist/(?P<playlist_id>\d+)/$', views.playlist, name='playlist'),
    url(r'^admin/', include(admin.site.urls)),
]