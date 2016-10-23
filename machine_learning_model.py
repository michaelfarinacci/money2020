import csv
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier


def train_ml_model():
	data_set = pd.DataFrame.from_csv('/Users/aga/Downloads/trainHistory.csv', index_col=False, sep=',')
	feature_set = pd.DataFrame.from_csv('/Users/aga/Repos/money2020/money2020/data/sample.csv', index_col=False, sep=',')
	# amount_sum = feature_set.groupby(['id'])['purchaseamount'].sum()

	train_data, test_data, train_target, test_target = train_test_split(data_set, data_set['repeater'],
                                                                                          test_size=0.2,
                                                                                          random_state=1)

	feature_columns = ['category', 'company', 'date', 'purchasequantity', 'purchaseamount']

# 	# Merge with features
	train_features = pd.merge(train_data, feature_set, how='left', on=['id', 'chain'])
	train_features = train_features[pd.notnull(train_features['company'])]
	train_features = train_features[feature_columns] # Keep only feature columns - no cheating!
	print train_features.head()

	print test_data.head()
	test_features = pd.merge(test_data, feature_set, how='left').set_index('id')
	test_features = test_features[pd.notnull(test_features['company'])]
	test_features = test_features[feature_columns]
	print test_features.head()

# 	train_features = feature_set[feature_set['id']]

# 	amount_sum = feature_set.groupby(['id'])['amount'].sum()
# 	amount_median = feature_set.groupby(['id'])['amount'].median()
# 	amount_max = feature_set.groupby(['id'])['amount'].max()
# 	amount_min = feature_set.groupby(['id'])['amount'].max()

# 	params = {
#         'n_estimators': 1500,
#         'bootstrap': True,
#         'min_samples_leaf': 1,
#         'max_features': "sqrt",
#         'criterion': "gini",
#         'min_samples_split': 3,
#         'max_depth': 10,
#         'class_weight': "auto"
#     }

#     # Create and train the model
#     forest = RandomForestClassifier(**params)
#     forest = forest.fit(train_features, train_target)

#     # Make predictions on test data
#     predicted = forest.predict(test_features)


# def total_spent_feature(features_frame):
# 	features_frame['total_spent'] = features_frame


# def predict_repeating_customers(customer_info, ml_model):
# 	predictions = ml_model.predict(customer_info)


if __name__ == '__main__':
	train_ml_model()



