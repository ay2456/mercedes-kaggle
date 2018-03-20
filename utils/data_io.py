import pandas as pd
from utils import constants


def load_train():
    df = pd.read_csv(constants.DATA_FILE_PATH + "/data/train.csv")
    return df

def load_test():
    df = pd.read_csv(constants.DATA_FILE_PATH + "/data/test.csv")
    return df