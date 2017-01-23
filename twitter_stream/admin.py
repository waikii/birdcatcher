from django.contrib import admin

# Register your models here.

from twitter_stream.models import tweet

admin.site.register(tweet)