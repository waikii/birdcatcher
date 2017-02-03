from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from .models import tweet
import datetime
import twitter_stream
import stream
import json


# Create your views here.

# Display the received tweets

def index(request):
  #  try:
  #      import json
  #  except ImportError:
  #      import simplejson as json
        
    # Open the json file for reading 
    
   # with open('twitter_stream_1000tweets.json') as json_file:  
        
    # Assign the json data to variable tweet
   
    tweets = tweet.objects.all()
    
    # Define arrays
    tweet_text = []
    tweet_profile_picture = []
    tweet_expand_url = []
    tweet_image = []
    
    # Iterate through the tweets
    
    for n in range(len(tweets)):
        tweet_text.append(tweets[n].tweet_text)
        tweet_profile_picture.append(tweets[n].tweet_profile_picture)
        tweet_expand_url.append(tweets[n].tweet_expand_url)
        tweet_image.append(tweets[n].tweet_image)
        
        
    template = loader.get_template('index.html')

# range in context is used for iterating over each tweet

    context = Context({"tweet": tweet_text,  "tweet_profile":tweet_profile_picture,"twitterretweet":tweet_expand_url,"tweet_image": tweet_image, "four": range(4), "range": range(len(tweet_text))})


    return HttpResponse(template.render(context))