from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    password = models.CharField(max_length=32)

class MyUser(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField("first_name", max_length=30, blank=False)
    last_name = models.CharField("last_name", max_length=30, blank=False)
    date_of_birth = models.DateField(blank=False)

    def __unicode__(self):
        return u'%s' %(self.user)


class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)


class Album(models.Model):
    artist = models.ForeignKey(Artist)
    name = models.CharField(max_length=100)
    year = models.IntegerField(default=0)
    num_stars = models.IntegerField()

    class Meta:
        unique_together = ("name", "artist")


class Track(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist)
    album = models.ForeignKey(Album)
    track_no = models.IntegerField(default=0)


class Playlist(models.Model):
    name = models.CharField(max_length=200)
    pid = models.CharField(max_length=200)


