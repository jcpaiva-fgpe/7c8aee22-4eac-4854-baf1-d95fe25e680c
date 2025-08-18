import pandas as pd

def weights(path):
    # TODO this is what you need to complete
    total_value = df["Value"].sum()
    df["Weight"] = df["Value"] / total_value
    print(df[["Coin", "Weight"]])


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    weights(inp)
############## DO NOT TOUCH AREA: END ###################
