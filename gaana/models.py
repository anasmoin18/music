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
    city = models.CharField(max_length=60, null=True)
    state_province = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return u'%s' %(self.user)

class Song(models.Model):
    artist = models.CharField(max_length=30)
    album = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    size = models.IntegerField(blank=True, default=0)

    def __unicode__(self):
        return u'%s' %(self.artist)


