from __future__ import unicode_literals

from django.db import models

# Create your models here.

class tweet(models.Model):
    tweet_id = models.IntegerField(primary_key=True)
    tweet_text = models.CharField(max_length=145)
    tweet_profile_picture = models.CharField(max_length=2084)
    tweet_expand_url = models.CharField(max_length=2084)
    tweet_image = models.CharField(max_length=2084)
