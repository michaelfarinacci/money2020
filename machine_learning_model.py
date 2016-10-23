import csv
import pandas as pd
from sklearn.cross_validation import train_test_split


def get_data():
	data_set = pd.DataFrame.from_csv('/Users/aga/Downloads/trainHistory.csv')
	feature_set = pd.DataFrame.from_csv('/Users/aga/Repos/money2020/money2020/data/sample.csv')
	print feature_set.head()

	# Merge with features

	train_data, test_data, train_target, test_target = train_test_split(data_set, data_set['repeater'],
                                                                                          test_size=0.2,
                                                                                          random_state=1)

	# Drop target values in train and test data






if __name__ == '__main__':
	get_data()



