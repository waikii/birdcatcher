from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
import datetime
import twitter_stream
import stream
import json


# Create your views here.
from . import models as m

def index(request):
    try:
        import json
    except ImportError:
        import simplejson as            json
        
    
    with open('twitter_stream_1000tweets.json') as json_file:  
        tweet = json.load(json_file)
        tweet_text = []
        tweet_profile_picture = []
        tweet_expand_url = []
        tweet_image = []
        print len(tweet['statuses'])
        for n in range(len(tweet['statuses'])):
            tweet_text.append(tweet['statuses'][n]['text'])
            tweet_profile_picture.append(tweet['statuses'][n]['user']['profile_image_url_https'])
         
            try:
                tweet_expand_url.append(tweet['statuses'][n]['entities']['media'][0]['expanded_url'])
                tweet_image.append(tweet['statuses'][n]['entities']['media'][0]['media_url'])
            except KeyError:
                tweet_image.append("")
                tweet_expand_url.append("")
            
    template = loader.get_template('index.html')
    context = Context({"tweet": tweet_text,  "tweet_profile":tweet_profile_picture,"twitterretweet":tweet_expand_url,"tweet_image": tweet_image, "range": range(len(tweet_text))})
    
    return HttpResponse(template.render(context))