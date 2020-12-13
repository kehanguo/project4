#https://realpython.com/twitter-bot-python-tweepy/

import json
#import tweepy
import tweepy


# Authenticate to Twitter
auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")
# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")

#mark most recent tweet as liked
def favor():
    tweets = api.home_timeline(count=1)
    tweet = tweets[0]
    print(f"Liking tweet {tweet.id} of {tweet.author.name}")


#get most recent 10 filtered tweets from the stream.
def get_tweets():
    api.create_favorite(tweet.id)
    tweets_listener = MyStreamListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener) 
    stream.filter(track=["Boston University", "Engineering", "ECE"], languages=["en"])

    for tweet in tweepy.Cursor(api.home_timeline).items(10):
        print(f"{tweet.user.name} said: {tweet.text}")

#print the tweets blocked
def block_tweets():
    for block in api.blocks():
    print(block.name)

if __name__ == '__main__':
    favor()
    get_tweets()



