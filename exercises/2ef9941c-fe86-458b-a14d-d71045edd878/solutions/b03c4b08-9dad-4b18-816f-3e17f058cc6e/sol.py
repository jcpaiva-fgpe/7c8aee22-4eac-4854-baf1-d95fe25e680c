import pandas as pd

def missing_values(path):
    # TODO this is what you need to complete
    df["CO2"].fillna(df["CO2"].mean(), inplace=True)
    print(df["CO2"].isna().sum())


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    result = missing_values(inp)
    print(result)
############## DO NOT TOUCH AREA: END ###################
