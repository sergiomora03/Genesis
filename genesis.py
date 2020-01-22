import tweepy
import time
import feedparser

# Authenticate to Twitter
auth = tweepy.OAuthHandler("XXXXXXX", "XXXXXXXX")
auth.set_access_token("XXXXXXXX-XXXXXXXX", "XXXXXXXXXX")

# Name api

tweepy = tweepy.API(auth)

# Check credentials Twitter
try:
    tweepy.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# update_status - get the rss of the site 

def update_status():
	# save the content rss into data
	data = feedparser.parse("https://securityaffairs.co/wordpress/feed")
	# call the lastest title post
	title = data.entries[0].title
	# call the lastest link post
	link =data.entries[0].link
	# format text for tweet
	post = title + " - " + link
	#post tweet
	tweepy.update_status(post)
	# print stdout of tweet 
	print(post)

#update status 3 times of day. 
while True:
	update_status()
	time.sleep(28800)

