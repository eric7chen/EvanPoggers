import os
import tweepy as tw
import pandas as pd
from tweepy.streaming import StreamListener
from credentials import *

class NewTweetListener(tw.StreamListener):

    def __init__(self, api, user_id):
        super(StreamListener, self).__init__()
        self.api = api
        self.user_id = user_id
        self.word_sentiment = pd.read_csv('words.csv', header=None)

    def on_status(self, tweet):
        print(tweet.text)
        if tweet.user.id_str == self.user_id:
            self.reply(tweet)
        tweet.favorite()

    def reply(self, tweet):
            self.api.update_status(status = 'pogchamp', in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)

def main():

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    user = api.get_user(screen_name = '@airwickchen')
    user_id = user.id_str

    myStreamListener = NewTweetListener(api, user_id)
    myStream = tw.Stream(auth = auth, listener=myStreamListener)
    myStream.filter(follow=[user_id])

if __name__ == '__main__':
    main()