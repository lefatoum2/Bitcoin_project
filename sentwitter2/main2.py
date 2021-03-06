import json
import config
import requests
import datetime
import pandas as pd
import tweepy as tw
import streamlit as st
import matplotlib.pyplot as plt
from pydantic import BaseModel
from classify import remove_noise
from nltk.tokenize import word_tokenize
import utils as utils

classifier = utils.load_model()


# nltk.download("punkt")
# nltk.download("wordnet")
# nltk.download("stopwords")
# nltk.download("averaged_perceptron_tagger")


class Tweet(BaseModel):
    tweet: str


def analyse_tweet(tweet: Tweet):
    custom_tokens = remove_noise(word_tokenize(tweet))
    result = classifier.classify(dict([token, True] for token in custom_tokens))
    return {"sentiment": result}


auth = tw.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

st.title("Twitter Live Sentiment Visualizer (beta)")
st.sidebar.title("Enter a hashtag")
hashtag = st.sidebar.text_input("hashtag", "trump")
date = st.sidebar.date_input("Analyse tweets from", datetime.date(2020, 8, 1))

if st.sidebar.button("Live analysis", key="analyse"):
    pos_count = 0
    neg_count = 0
    tweets_count = 0

    st.subheader(f"Analysing #{hashtag} from {date}")
    d = {"Positive": [pos_count], "Negative": [neg_count]}
    df = pd.DataFrame(data=d)

    hashtag = f"#{hashtag}"
    with st.spinner("Getting tweets..."):
        tweets = tw.Cursor(api.search_tweets, q=hashtag, lang="en", since=date).items()

    total_tweets = st.empty()
    pos_tweets = st.empty()
    neg_tweets = st.empty()

    sentiments = ["Positive", "Negative"]
    chart = st.line_chart(df)
    barchart = st.empty()

    for idx, tweet in enumerate(tweets):
        tweets_count += 1
        output = "tweet :" + analyse_tweet(tweet.text)
        output = requests.post("analyse_tweet(tweet: Tweet)", json={"tweet": tweet.text})
        output = output.content.decode("utf8")
        output = json.loads(output).get("sentiment")

        if output == "Negative":
            neg_count += 1
        elif output == "Positive":
            pos_count += 1

        total_tweets.text("Tweets Analysed: %d" % tweets_count)
        pos_tweets.text("Positive tweets: %d" % pos_count)
        neg_tweets.text("Negative tweets: %d" % neg_count)

        df2 = pd.DataFrame({"Positive": [pos_count], "Negative": [neg_count]})
        df.update(df2)
        chart.add_rows(df)

    if neg_count == 0 and pos_count == 0:
        st.warning(f"No Tweets Found on {hashtag}")
    else:
        st.success("Tweets classified")
