import pandas as pd
import numpy as np
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"

def group(path):
    # TODO this is what you need to complete
    df = pd.read_csv(path)
    grouped = df.groupby("Name")[["High", "Low"]].mean()
    return grouped


############## DO NOT TOUCH AREA: START #################
def save_df(df):
    file_path = 'pandas_crypto_5_' + str(np.random.randint(1000)) + '.csv'
    df.to_csv(file_path, index=False)
    return file_path

if __name__ == '__main__':
    inp = input()
    df = group(inp)
    path = save_df(df)
    print(path)
############## DO NOT TOUCH AREA: END ###################
