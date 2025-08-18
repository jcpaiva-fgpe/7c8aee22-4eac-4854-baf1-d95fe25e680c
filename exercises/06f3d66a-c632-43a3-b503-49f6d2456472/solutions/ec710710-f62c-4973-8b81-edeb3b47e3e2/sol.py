import pandas as pd

def missing_data(path):
    # TODO this is what you need to complete
    df["CurrentPrice"].fillna(df["CurrentPrice"].mean(), inplace=True)


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    missing_data(inp)
############## DO NOT TOUCH AREA: END ###################
