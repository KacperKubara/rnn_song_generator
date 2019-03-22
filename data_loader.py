import pandas as pd
import os
# Generates data for train, validation and test datasets
class Data_Loader():
    def __init__(self, path, train_size = 0.7, test_size = 0.25):
        self.path = path
        if train_size < 1 and train_size > 0: 
            self.train_size = train_size
        else: train_size = 0.7
        if test_size < 1 - train_size and test_size > 0:
            self.test_size = test_size
        else: test_size = 0.25
        self.valid_size = 1 - train_size - test_size
    def save_data(self, column_name):
        exists = []
        exists.append(os.path.isfile("./datasets/test_data.csv"))
        exists.append(os.path.isfile("./datasets/train_data.csv"))
        exists.append(os.path.isfile("./datasets/valid_data.csv"))
        # Check if file already exists        
        if all(exists) is False:
            dataset = pd.read_csv(self.path)
            dataset = dataset[column_name]
            length = len(dataset)
            # Shuffle data 
            dataset = dataset.sample(frac=1).reset_index(drop=True)
            # Divide data into different datasets
            print(dataset.head())
            train_data = dataset[0 : int(self.train_size*length) - 1]
            test_data  = dataset[int(self.train_size*length) : int((self.train_size + self.test_size)*length) - 1]
            valid_data = dataset[int((self.train_size + self.test_size)*length) : -1] 
            # Save the datasets
            train_data.to_csv("./datasets/train_data.csv", index = False, header = [column_name])
            test_data.to_csv("./datasets/test_data.csv", index = False, header = [column_name])
            valid_data.to_csv("./datasets/valid_data.csv", index = False, header = [column_name])
        

