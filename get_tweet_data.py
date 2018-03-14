import pandas as pd
import numpy as np
import tweepy
import cnfg
import time
import datetime
from textblob import TextBlob


config = cnfg.load(".twitter_config")
auth = tweepy.OAuthHandler(config["consumer_key"],
                           config["consumer_secret"])
auth.set_access_token(config["access_token"],
                      config["access_token_secret"])
api = tweepy.API(auth)
year = "2018"

teams = pd.read_csv("Input/march_madness_twitter_handles_" + year + ".csv")
team_list = teams.twitter_handle.tolist()


data = []
for count, team in enumerate(team_list):
	print (team + ": " + str(count + 1) + "/" + str(len(team_list) - 1) + " finished")
	try:
		user = api.get_user(team)
		retweets = []
		polarity = []
		for tweet in tweepy.Cursor(api.user_timeline, id= team, wait_on_rate_limit=True).items(100):
		    retweets.append(tweet.retweet_count)
		    polarity.append(TextBlob(tweet.text).sentiment.polarity)
		retweet_avg = np.mean(retweets)
		polarity_avg = np.mean(polarity)
		data.append({'username': user.screen_name,
		             'num_followers': user.followers_count,
		             'num_favorites': user.favourites_count,
		             'num_friends': user.friends_count,
		             'num_statuses': user.statuses_count,
		             'retweet_avg': retweet_avg, 
		             'polarity_avg': polarity_avg})
	except tweepy.TweepError:
		print ("Sleeping because of", team, "time:", datetime.datetime.now().time())
		pass

tweet_df = pd.DataFrame(data)
tweet_df.username = tweet_df.username.str.lower()
df = teams.merge(tweet_df, left_on = "twitter_handle", right_on = "username", how = "left" )
df = df.drop(["username"], axis = 1)
df.to_csv("Output/march_madness_tweet_data_" + year + ".csv", index = False)