import tweepy
import random
import json
import time

# Twitter credentials goes here
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'quotes.json'

def get_quote(file_name):
    f = open(FILE_NAME)
    data = json.load(f)
    data_size = len(data['quotes'])
    rand = random.randrange(1,data_size)
    random_quote = data['quotes'][rand]
    tweet = random_quote['text'] + ' - #' + random_quote['author']
    f.close()
    return tweet

while (True):
    tweet_data = get_quote(FILE_NAME)
    if (len(tweet_data) > 280):
        continue
    else:
        print("posting tweet...")
        try:
            if api.update_status(tweet_data):
                print("tweet posted successfully!")
        except tweepy.error.TweepError as e:
            print(e.reason)
        
        time.sleep(3600) #Adjust this time to set interval between tweets