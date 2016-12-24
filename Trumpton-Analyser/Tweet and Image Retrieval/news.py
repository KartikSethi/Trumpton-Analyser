""" 
	File to retrieve image URLs from various news handles.
	Follows the same approach as 'tweet_access.py'
"""

import tweepy
import json
import time

consumer_key = 'dxwye8KuUDcp4bYvdHxhYFqR5'
consumer_secret = 'UDCmi8CgCBnD4ZeAlFyJ9BKuib95os4gMdGsgx8gVuVhSCYyFm'
access_token = '140766292-IfJjlG517oBhu7HccICBuMqpHeAQdGmdPYHYCByY'
access_token_secret = 'yOqnqBCZqrZSWum9wOySzCQT8btW9j1gYgXDTPIJ6vkAf'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


id_images=[]
news_handles =  ['@BBC', '@BBCBreaking', '@BBCWorld', '@BBCNews', '@Reuters', '@ReutersWorld', '@AJEnglish', '@AJENews', '@FoxNews'] #['@CNN', '@cnnbrk', '@CNNPolitics', '@cnni', '@CNNnews18',
f_h = open('news/hillary/output.txt', 'a')
f_t = open('news/trump/output.txt', 'a')
f_b = open('news/both/output.txt', 'a')
f_n = open('news/none/output.txt', 'a')
h = 'hillary'
t = 'trump'


for handle in news_handles:
	h_count=0
	t_count=0
	n_count=0
	b_count=0
	print "Current Handle is " + str(handle)
	tweets = api.user_timeline(handle, count = 200, include_rts = False, exclude_replies=True)
	last_id = tweets[-1].id
	# since_id = tweets[-1].id


	while(True):
		try:
			public_tweets = api.user_timeline(handle, count = 200, include_rts = False, exclude_replies=True,max_id=last_id-1)
		except:
			time.sleep(3)
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
	for i in all_items:
		try:
			text = i.text
			if 'media' in i.entities:
				if i.entities['media'][0]['type'] == 'photo':
					media_files.add(i.entities['media'][0]['media_url'])
					if ((h in text.lower()) and  (t in text.lower())):
						# print "Both"
						f_b.write(i.entities['media'][0]['media_url'])
						f_b.write('\n')
						b_count += 1
					elif h in text.lower():
						# print "Hillary"
						f_h.write(i.entities['media'][0]['media_url'])
						f_h.write('\n')
						h_count += 1
					elif t in text.lower():
						# print "Trump"
						f_t.write(i.entities['media'][0]['media_url'])
						f_t.write('\n')
						t_count += 1
					else:
						# print "None"
						f_n.write(i.entities['media'][0]['media_url'])
						f_n.write('\n')
						n_count += 1
		except:
			pass
	print "H count: " + str(h_count)
	print "T count: " + str(t_count)
	print "B count: " + str(b_count)
	print "N count: " + str(n_count)
	time.sleep(3)

# print media_files
# f.close()
# print tweets_images