"""
	File to retrieve the image URLs from the 'python.json' (collection of tweets)
	file created using hash.py
"""

file_hillary = open('hash/hillary/output2.txt', 'w') 
file_trump = open('hash/trump/output2.txt', 'w')
file_both = open('hash/both/output2.txt', 'w')
file_none = open('hash/none/output2.txt', 'w')
h = 'hillary'
t = 'trump'
import json
h_count=0
t_count=0
n_count=0
b_count=0
f = open('python.json','r')
for line in f:
	try:
	  	tweets=[] 
	  	tweets.append(json.loads(line))
		text = tweets[0]['text']
		# checking the presence of media then selecting image files with 
		# tweet text = 'hillary' or 'trump' or both
		if 'media' in tweets[0]['entities']:
			if tweets[0]['entities']['media'][0]['type'] == 'photo':
				if (h in text.lower()) and  (t in text.lower()):
					# print "Both"
					file_both.write(tweets[0]['entities']['media'][0]['media_url'])
					file_both.write('\n')
					b_count+=1
				elif h in text.lower():
					# print "Hillary"
					file_hillary.write(tweets[0]['entities']['media'][0]['media_url'])
					file_hillary.write('\n')
					h_count+=1
				elif t in text.lower():
					# print "Trump"
					file_trump.write(tweets[0]['entities']['media'][0]['media_url'])
					file_trump.write('\n')
					t_count+=1
				else:
					# print "None"
					file_none.write(tweets[0]['entities']['media'][0]['media_url'])
					file_none.write('\n')
					n_count+=1

	except:
		pass

print "Both count: " + str(b_count)
print "Hillary count: " + str(h_count)
print "Trump count: " + str(t_count)
print "None count: " + str(n_count)
