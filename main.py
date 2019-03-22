from data_loader import Data_Loader
if __name__ == "__main__":
    loader = Data_Loader(path = "./datasets/articles1.csv")
    loader.save_data("content")