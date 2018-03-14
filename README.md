How to use:
1. Make march_madness_twitter_handles_<THIS_YEAR>.csv file including seed, conference, team name, and Twitter handle.
2. Run get_tweet_data.py to get data from Twitter.
3. Make march_madness_results_<LAST_YEAR>.csv by adding the round each team reached in last year's tournament.
4. Run create_prior_year_model.py to make a model based on which features were most predictive last year.
5. Run add_features.py to rank the Twitter features, add a rank based on the previous year's model and make the final predictions.
6. Use results to make your bracket and win!


## TO DO
1. Build scraper to get bracket team names, seeds and divisions.
2. Scrape Twitter handles of men's basketball team.
	- Generally the top Google search of "<team name> ncaa men's basketball Twitter" is the handle.
	- Might want to verify that the top account is the one tweeting about March Madness.  Sometimes there are multiple accounts at a school.  Maybe check for recent #MarchMadness tweet?
3. Modify get_tweet_data.py to recheck handles if it was initially skipped due to rate limits.
4. Use TextBlob (or other similar package) to measure sentiment of recent tweets and add to model.
5. Scrape prior years results.
	- Currently using round reached
	- Consider adding scores as result
6. Explore adding new features:
	- Number of times school has reached the tournament