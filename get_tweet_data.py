import pandas as pd
import numpy as np
import tweepy
import cnfg
import time
import datetime


config = cnfg.load(".twitter_config")
auth = tweepy.OAuthHandler(config["consumer_key"],
                           config["consumer_secret"])
auth.set_access_token(config["access_token"],
                      config["access_token_secret"])
api = tweepy.API(auth)
year = "2018"

teams = pd.read_csv("Input/march_madness_twitter_handles_" + year + "_1.csv")
team_list = teams.twitter_handle.tolist()


data = []
for count, team in enumerate(team_list):
	print (team + ": " + str(count) + "/" + str(len(team_list)) + " finished")
	try:
		user = api.get_user(team)
		screen_name = user.screen_name
		num_followers = user.followers_count
		num_favorites = user.favourites_count
		num_friends = user.friends_count
		num_statuses = user.statuses_count
		retweets = []
		for tweet in tweepy.Cursor(api.user_timeline, id= team, wait_on_rate_limit=True).items(100):
		    retweets.append(tweet.retweet_count)
		retweet_avg = np.mean(retweets)
		data.append({'username': screen_name, 
		          'num_followers': num_followers, 
		          "num_favorites": num_favorites,
		          "num_friends": num_friends, 
		          "num_statuses": num_statuses,
		          'retweet_avg': retweet_avg})   
	except tweepy.TweepError:
		print ("Sleeping because of", team, "time:", datetime.datetime.now().time())
		pass

tweet_df = pd.DataFrame(data)
tweet_df.username = tweet_df.username.str.lower()
df = teams.merge(tweet_df, left_on = "twitter_handle", right_on = "username", how = "left" )
df = df.drop(["username"], axis = 1)
df.to_csv("Output/march_madness_tweet_data_" + year + "_1.csv", index = False)