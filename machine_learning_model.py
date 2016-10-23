import csv
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np


def train_ml_model():
    data_set = pd.DataFrame.from_csv('/Users/aga/Downloads/trainHistory.csv', index_col=False, sep=',')
    feature_set = pd.DataFrame.from_csv('/Users/aga/Repos/money2020/money2020/data/sample.csv', index_col=False, sep=',')
    features_merged = pd.merge(data_set, feature_set, how='left', on=['id', 'chain'])


    features_merged.fillna(0, inplace=True)
    # feature_columns = ['id', 'chain', 'category', 'company', 'date', 'purchasequantity', 'purchaseamount']
    feature_columns = ['id', 'chain', 'purchasequantity', 'purchaseamount']

    train_data, test_data, train_target, test_target = train_test_split(features_merged[feature_columns], features_merged['repeater'],
                                                                                          test_size=0.2,
                                                                                          random_state=1)

# amount_sum = feature_set.groupby(['id'])['amount'].sum()
# amount_median = feature_set.groupby(['id'])['amount'].median()
# amount_max = feature_set.groupby(['id'])['amount'].max()
# amount_min = feature_set.groupby(['id'])['amount'].max()

	# params = {
 #        'n_estimators': 1500,
 #        'bootstrap': True,
 #        'min_samples_leaf': 1,
 #        'max_features': "sqrt",
 #        'criterion': "gini",
 #        'min_samples_split': 3,
 #        'max_depth': 10,
 #        'class_weight': "auto"
 #    }

    # Create and train the model
    print "Creating the model..."
    forest = RandomForestClassifier(n_estimators=100, max_depth=3)
    print "Created the model"
    # train_data = train_data['id', 'chain', 'purchaseamount']
    print "Training the model..."
    forest = forest.fit(train_data, train_target)
    print "Trained the model"

#     # Make predictions on test data
    # predicted = forest.predict(test_features)


def predict_repeating_customers(customer_info, ml_model):
	predictions = ml_model.predict(customer_info)

	# TODO: Save predictions in the db...


if __name__ == '__main__':
	train_ml_model()



