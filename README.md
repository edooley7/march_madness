
## HOW TO USE:
1. Make march_madness_twitter_handles_<THIS_YEAR>.csv file including seed, conference, team name, and Twitter handle.
2. Run get_tweet_data.py to get data from Twitter and output march_madness_tweet_data_<THIS_YEAR>.csv
3. Make march_madness_results_<LAST_YEAR>.csv by adding the round each team reached in last year's tournament.
4. Run create_prior_year_model.py to make a model based on which features were most predictive last year.  This will output march_madness_model_<LAST_YEAR>.pickle and march_madness_predictions_<LAST_YEAR>.csv.
5. Run add_features.py to rank the current year Twitter features, add a rank based on the previous year's model and make the final predictions.  This will output march_madness_final_predictions_<THIS_YEAR>.csv
6. Use results to fill out your bracket and win!


## TO DO
Pull requests and other collaboration more than welcome!
1. Build scraper to get bracket team names, seeds and divisions.
2. Scrape Twitter handles of men's basketball team.
	- Generally the top Google search of "<team name> ncaa men's basketball Twitter" is the handle.
	- Might want to verify that the top account is the one tweeting about March Madness.  Sometimes there are multiple accounts at a school.  Maybe check for recent #MarchMadness tweet?
3. Incorporate average tweet sentiment into the model.
4. Scrape prior years results.
	- Currently pulling by hand from Wikipedia
	- Currently using round reached
	- Consider adding scores as result
5. Explore adding new features:
	- Number of times school has reached the tournament
6. See if adding multiple years of tweet data is feasible or helpful.