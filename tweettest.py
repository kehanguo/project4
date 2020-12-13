import pytest
import tweetAPIexample as API
import sentiment_analysis as NLP
import os
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

api = API.Authorization_Setup()
with open('Hashtag_Tweets.json') as f:
  testdata = json.load(f)

#standard unit test of search function of API using return value for successful query
def standard_test_API():
    assert API.GET_Hashtag_Search_Tweets(api,"#BU","recent",5,"2020-12-10") == testdata,"Error")

#Checking if there is information present to analyze
def sentiment_test_empty():
    assert os.path.getsize("./Hashtag_tweets.json") != 0, "File w/ Tweets is empty"
