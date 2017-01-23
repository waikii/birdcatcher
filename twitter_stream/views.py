from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
import datetime
import twitter_stream
import stream
import json


# Create your views here.
from . import models as m

# Display the received tweets

def index(request):
    try:
        import json
    except ImportError:
        import simplejson as json
        
    # Open the json file for reading 
    
    with open('twitter_stream_1000tweets.json') as json_file:  
        
        # Assign the json data to variable tweet
        
        tweet = json.load(json_file)
        
        # Define arrays
        
        tweet_text = []
        tweet_profile_picture = []
        tweet_expand_url = []
        tweet_image = []
        
        # Iterate through the tweets
        
        for n in range(len(tweet['statuses'])):
            tweet_text.append(tweet['statuses'][n]['text'])
            tweet_profile_picture.append(tweet['statuses'][n]['user']['profile_image_url_https'])
            
            # If the json has information about media, the append it to their arrays
            
            try:
                tweet_expand_url.append(tweet['statuses'][n]['entities']['media'][0]['expanded_url'])
                tweet_image.append(tweet['statuses'][n]['entities']['media'][0]['media_url'])
            
            #If the json has no information about media then append an empty string
            
            except KeyError:
                tweet_image.append("")
                tweet_expand_url.append("")
            
    template = loader.get_template('index.html')
    
    # range in context is used for iterating over each tweet
    
    context = Context({"tweet": tweet_text,  "tweet_profile":tweet_profile_picture,"twitterretweet":tweet_expand_url,"tweet_image": tweet_image, "range": range(len(tweet_text))})
    
    return HttpResponse(template.render(context))