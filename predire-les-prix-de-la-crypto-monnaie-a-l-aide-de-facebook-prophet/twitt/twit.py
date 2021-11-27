import streamlit as st
import tweepy
import pandas as pd
from textblob import TextBlob

API_KEY = '3OvA1OXH8vkMSHSSmZUjwZVJK'
SECRET_KEY = 'qQhAz8nk5iiGjAIKDg7rb8JpXl2EaLTCNQLgXJDEHkuYPT6oOl'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAN5EVwEAAAAAI%2F2zOWSTTnzNl4iUc4hZoNndMxg%3DaLdhFfFh8tI4dfAqfNznqtCiZV6l4J7fhHrJbHCf3pBcjazSsb'
ACCESS_TOKEN = '2327890302-HnmMaCTEPZvqs7jfsLzPvnZWUqrYmDenSqnMPtQ'
SECRET_TOKEN = 'ZoYbVzcAn5kbkmUwOQqb1ZnltZUonaQOqTYJdVVpqV1XC'

auth = tweepy.OAuthHandler(API_KEY, SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, SECRET_TOKEN)
api = tweepy.API(auth)


# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#    print(tweet.user.name, tweet.text)


def fetch_tweets(hashtag):
    tweet_user = []
    tweet_time = []
    tweet_string = []

    for tweet in tweepy.Cursor(api.search, q=hashtag, count=5000).items(5000):
        if (not tweet.retweeted) and ("RT @" not in tweet.text):
            if tweet.lang == "en":
                tweet_user.append(tweet.user.name)
                tweet_time.append(tweet.created_at)
                tweet_string.append(tweet.text)

    df = pd.DataFrame({"username": tweet_user, "time": tweet_time, "tweet": tweet_string})
    return df


df = fetch_tweets("bitcoin")

df["sentiment"] = df["tweet"].apply(lambda tweet: TextBlob(tweet).sentiment.polarity)

df = df[["time", "sentiment"]]

st.line_chart(df)
