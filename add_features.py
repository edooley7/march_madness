# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <codecell>

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

# <codecell>

this_year = '2018'
last_year = str(int(this_year)-1)

# <codecell>

df = pd.read_csv('Output/march_madness_tweet_data_' + this_year + '.csv')

# <codecell>

# Rank all features
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

# Use prior year model to predict this years results
prior_year_model = pd.read_pickle('Output/march_madness_model_' + last_year + '.pickle')
x = df[all_features]
df['py_model_prediction'] = prior_year_model.predict(x)
df['py_model_prediction_rank'] = df.py_model_prediction.rank()

# <codecell>

# Export current year predictions
df.to_csv('Output/march_madness_final_predictions_' + this_year + '.csv')

# <codecell>


