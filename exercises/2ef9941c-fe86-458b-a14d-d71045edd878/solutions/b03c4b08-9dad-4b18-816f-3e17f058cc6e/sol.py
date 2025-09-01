import pandas as pd
import numpy as np
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"

def missing_values(path):
    # TODO this is what you need to complete
    df = pd.read_csv(path)
    df["CO2"].fillna(df["CO2"].mean(), inplace=True)
    return df


############## DO NOT TOUCH AREA: START #################
def save_df(df):
    file_path = 'pandas_climate_6_' + str(np.random.randint(1000)) + '.csv'
    df.to_csv(file_path, index=False)
    return os.path.abspath(file_path)

if __name__ == '__main__':
    inp = input()
    df = missing_values(inp)
    path = save_df(df)
    print(path)
############## DO NOT TOUCH AREA: END ###################
