"""
	File to retrieve image URLs from '@HillaryClinton' and '@realDonalTrump' handles
"""

import tweepy
import json
import time

consumer_key = <write yours here> # sorry can't share these
consumer_secret = <write yours here>
access_token = <write yours here>
access_token_secret = <write yours here>

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets_images=[]
id_images=[]

# change the screen_name to '@realDonaldTrump' to access images from Trump's handle
tweets = api.user_timeline(screen_name="@HillaryClinton", count = 200, include_rts = False, exclude_replies=True)
last_id = tweets[-1].id
since_id = tweets[-1].id


while(True):
	
	try:
		public_tweets = api.user_timeline(screen_name="@HillaryClinton", count = 200, include_rts = False, exclude_replies=True,max_id=last_id-1)
	except:
		time.sleep(2)
		continue
	if(len(public_tweets) == 0):
		break
	else:
			last_id = public_tweets[-1].id - 1
			tweets = tweets + public_tweets
	print 'Tweet count:' + str(len(tweets))
	# time.sleep(2)

all_items=[]
[all_items.append(i) for i in tweets]
# print all_items.entities

# print str(type(all_items))
media_files = set()

f = open('hillary_out.txt', 'w')


for i in all_items:
	try:
		if i.entities['media'][0]['type'] == 'photo':
			media_files.add(i.entities['media'][0]['media_url'])
			f.write(i.entities['media'][0]['media_url'])
			f.write('\n')
			# tweets_images.append({'url':i.entities['media'][0]['media_url'],'id':i.id})
			# id_images.append(i.id)
	except:
		pass

print media_files
f.close()
# print tweets_images