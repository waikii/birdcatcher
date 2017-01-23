try:
         import json
except ImportError:
        import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError,TwitterStream

# Variables that contains the user credentials to access Twitter API

ACCESS_TOKEN = '235228993-UMgntnuS8UKyGU7pitxvMNxQO4Eqte2tgAGk9ijK'
ACCESS_SECRET = '9I8YOVtb6zIZaPpQEnAdVOZaq6vNBZJZVaRiU2OZir8os'
CONSUMER_KEY = 'pPa5GLuxOLzK57woQ1pdYQIAf'
CONSUMER_SECRET = 'IAsBqLL6lOQdcZ4VRu1ZIPvTOMIDw2Pa4bMbPtXbxP8Xwkjjd6'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)



twitter = Twitter(auth=oauth)

# Search queries to be parsed by Twitter API

recent_posts = twitter.search.tweets(q='from:@hm_morgan', result_type='recent', lang='en', count=4)
recent_posts2 = twitter.search.tweets(q='from:@hsru_aberdeen', result_type='recent', lang='en', count=5)

# Iterate for the length of array to extract the differen tweets

for n in range(len(recent_posts2['statuses'])):
    
    # append all tweets into one file
    
    recent_posts['statuses'].append(recent_posts2['statuses'][n])

# Open or create text file

text_file = open("twitter_stream_1000tweets.json", "w")

# Write the json dump to this text file

text_file.write(json.dumps(recent_posts))

# Close file

text_file.close()

