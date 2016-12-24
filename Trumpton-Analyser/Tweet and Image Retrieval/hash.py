"""
    File to store the tweets using stream API and then retrieving the media (images)
    with tweet text containg 'hillary' or 'donald' or both
"""

from tweepy import Stream
from tweepy.streaming import StreamListener
from httplib import IncompleteRead
import tweepy
import json
import time

consumer_key = <write yours> # sorry can't share these
consumer_secret = <write yours>
access_token = <write yours>
access_token_secret = <write yours>

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweet_count = 1

class MyListener(StreamListener):
 
    def on_data(self, data):
        global tweet_count
        print "Tweet Count: " + str(tweet_count)
        tweet_count += 1
        try:
            with open('python.json', 'a') as f: # writing the tweet data in a json file
                print data[19:35]
                f.write(data)
                f.write('\n')
                return True
        
        except BaseException as e:
            print("error: " + str(e))
            return True
 
    def on_error(self, status):
        print "error status " + str(status)
        time.sleep(2)
        return True
 
while True:
    try:
        twitter_stream = Stream(auth, MyListener())
        twitter_stream.filter(track=['#USElection', 'realDonaldTrump', 'HillaryClinton', '#HillaryClinton', 'Donald Trump', 'Hillary Clinton', 'donald trump', 'hillary clinton', '#MakeAmericaGreatAgain','#DonaldTrump'])
    except KeyboardInterrupt:
        twitter_stream.disconnect()
        break
    except:
        pass
    