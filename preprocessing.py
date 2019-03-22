import pandas as pd 
import collections
# Preprocesses the dataset
class Preprocessor():
    def __init__(self, batch_size = 30):
        self.path = path
        self.train_size = train_size
        # self.batch_size = batch_size
    # def generate_batch(self)
    def load_data(self):
        exists = []
        exists.append(os.path.isfile("./datasets/test_data.csv"))
        exists.append(os.path.isfile("./datasets/train_data.csv"))
        exists.append(os.path.isfile("./datasets/valid_data.csv"))
        if (all(exists) is True):
            # Create the vocab
            word_to_id = build_vocabulary()
            # Map words to integer keys
            
            # Create reversed vocab (keys and values are swapped)
            
            # Return the data
            return train_data, valid_data, test_data, vocabulary, reversed_dictionary
        else:
            print("Error in preprocessing.py, datasets have not been found")
    def build_vocabulary(self, path = "./datasets/train_data.csv"):
        # Check and finish this 
        data = read_words(path)
        counter = collections.Counter(data)
        count_pairs = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
        words, _ = list(zip(*count_pairs))
        word_to_id = dict(zip(words, range(len(words))))
        return word_to_id 
        
    def read_words(self, path):
        with open(path, "r") as f:
            return f.read().decode("utf-8").split()

        return vocabulary
    def file_to_word_ids(self):
        pass