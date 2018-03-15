import pandas as pd


def load_train():
    df = pd.read_csv("../data/train.csv")
    return df

def load_test():
    df = pd.read_csv("../data/test.csv")
    return df