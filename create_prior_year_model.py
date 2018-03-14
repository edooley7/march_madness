# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <codecell>

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import StandardScaler
import pickle

# <codecell>

round_dict = {1:1,
              2:2,
              4:3,
              8:4,
              16:5,
              32:6,
              64:7}

# <codecell>

this_year = '2018'
last_year = str(int(this_year)-1)

# <codecell>

# Read and combine last year's data
results_df = pd.read_csv('Input/march_madness_results_' + last_year + '.csv')
twitter_df = pd.read_csv('Input/march_madness_tweet_data_' + last_year + '.csv')
df = twitter_df.merge(results_df,
                      how = 'left', 
                      on = ['seed', 
                            'conference',
                            'seed_conference',
                            'team', 
                            'twitter_handle'])

# <codecell>

# Add ranks for prior year Twitter data
tweet_features = ['num_favorites', 'num_followers', 'num_friends', 'num_statuses', 'retweet_avg', 'seed']
rank_features = [feature + "_rank" for feature in tweet_features]
all_features = tweet_features + rank_features
for feature in tweet_features:
    if feature != 'seed':
        df[feature + "_rank"] = df[feature].rank(ascending = False)
    else:
        df[feature + "_rank"] = df[feature].rank(ascending = True)
df['average_rank'] = df[rank_features].mean(axis = 1)

# <codecell>

# Make a linear round_reached feature for reference
df['round_reached_linear'] = df.round_reached.map(round_dict)

# <codecell>

# Set up features to predict
y = df.round_reached
x = df[all_features]

standard_scaler = StandardScaler()
x = standard_scaler.fit_transform(x)

# <codecell>

# Fit and score model
model = LinearRegression()
model.fit(x, y)
print('Model accuracy: ', model.score(x, y))

# <codecell>

# Export model for use on current year data
with open('Output/march_madness_model_' + last_year + '.pickle', 'wb') as filename:
    pickle.dump(model, filename)

# <codecell>

# Export features and results together for exploration
df['py_model_prediction'] = model.predict(x)
df['py_model_prediction_rank'] = df.py_model_prediction.rank()
df = df.sort_values('round_reached')
df.to_csv('Output/march_madness_predictions_' + last_year + '.csv')

# <codecell>


