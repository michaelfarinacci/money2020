import csv
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn import metrics



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
    train_data['amount_sum'] = train_data.groupby(['id'])['purchaseamount'].sum()
    train_data['amount_median'] = train_data.groupby(['id'])['purchaseamount'].median()
    train_data['amount_max'] = train_data.groupby(['id'])['purchaseamount'].max()
    train_data['amount_min'] = train_data.groupby(['id'])['purchaseamount'].min()

    params = {
        'n_estimators': 100,
        # 'bootstrap': True,
        # 'min_samples_leaf': 1,
        # 'max_features': "sqrt",
        # 'criterion': "gini",
        'min_samples_split': 3,
        'max_depth': 5,
        'class_weight': "auto"
    }

    # Create and train the model
    print "Creating the model..."
    forest = RandomForestClassifier(**params)
    print "Created the model"
    # train_data = train_data['id', 'chain', 'purchaseamount']
    print "Training the model..."
    train_data.fillna(0, inplace=True)
    forest = forest.fit(train_data, train_target)
    print "Trained the model"

    test_data['amount_sum'] = test_data.groupby(['id'])['purchaseamount'].sum()
    test_data['amount_median'] = test_data.groupby(['id'])['purchaseamount'].median()
    test_data['amount_max'] = test_data.groupby(['id'])['purchaseamount'].max()
    test_data['amount_min'] = test_data.groupby(['id'])['purchaseamount'].min()
    test_data.fillna(0, inplace=True)

    # Make predictions on test data
    predicted = forest.predict(test_data)
    print metrics.classification_report(test_target, predicted, labels=['t', 'f'], target_names=['likely_to_purchase', 'unlikely_to_purchase'])
    predicted_proba = forest.predict_proba(test_data)
    print predicted_proba


def predict_repeating_customers(customer_info, ml_model):
	customer_features = customer_info['id', 'chain', 'purchaseamount', 'purchasequantity']
	# Returns a pandas data frame with customer_id, chain_id and score
	predictions = ml_model.predict(customer_features)
	return predictions
	# TODO: Save predictions in the db...


if __name__ == '__main__':
	train_ml_model()



