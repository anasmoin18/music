from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout, login
from gaana.models import *
from forms import SignUpForm


def home(request):
    return render_to_response('gaana/home.html',
                              {'user': request.user})


def sign_up(request):
    if request.method == 'POST':
        print request.POST
        data = request.POST.copy()
        data['username'] = data['username']
        form = SignUpForm(data)

        if form.is_valid():
            user = form.save()
            return render_to_response('gaana/sign_up_success.html')
    else:
        form = SignUpForm()

    return render_to_response('gaana/sign_up.html',
                              {'form': form},
                              context_instance=RequestContext(request))


def login(request):
    return render_to_response('registration/login.html',
                              {'user': request.user})


def albums(request):
    albums = Album.objects.all().order_by('name')
    return render_to_response('gaana/index.html',
                              {'list': albums, 'view':'album'},
                              context_instance=RequestContext(request))

def artist(request,artist_id):
    artist = Artist.objects.get(id=artist_id)
    albums = Album.objects.filter(artist=artist)
    return render_to_response('gaana/index.html',
                              {'list': albums, 'view':'album', 'artist': artist},
                              context_instance=RequestContext(request))

def playlists(request):
    playlists = Playlist.objects.all()
    return render_to_response('gaana/index.html',
                              {'list': playlists, 'view':'playlist'},
                              context_instance=RequestContext(request))

def playlist(request,playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    tracks = [pc.track for pc in PlaylistConnection.objects.filter(playlist=playlist)]
    return render_to_response('gaana/playlist.html',
                              {'playlist': playlist, 'tracks': tracks, 'view': 'single_playlist'},
                              context_instance=RequestContext(request))

def album(request,album_id):
    album = Album.objects.get(id=album_id)
    tracks = Track.objects.filter(album=album).order_by('track_no')
    return render_to_response('gaana/album.html',
                              {'album': album, 'tracks': tracks, 'view': 'single_album'},
                              context_instance=RequestContext(request))

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


