# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gaana', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.IntegerField(default=0)),
                ('num_stars', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pid', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('track_no', models.IntegerField(default=0)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaana.Album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaana.Artist')),
            ],
        ),
        migrations.DeleteModel(
            name='Song',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='city',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='country',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='state_province',
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaana.Artist'),
        ),
        migrations.AlterUniqueTogether(
            name='album',
            unique_together=set([('name', 'artist')]),
        ),
    ]
