# loads the text data from csv files, preprocesses it and splits it into train, test and validation datasets
class Preprocessor():
    def __init__(self, path, train_size = 0.7, batch_size = 30):
        self.path = path
        self.train_size = train_size
        # self.batch_size = batch_size
    # def generate_batch(self)
    def load_data(self):
        return train_data, test_data