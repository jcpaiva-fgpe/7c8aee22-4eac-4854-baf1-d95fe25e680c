import pandas as pd

def total(path):
    # TODO this is what you need to complete
    df["Value"] = df["Amount"] * df["CurrentPrice"]
    print(df["Value"].sum())


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    total(inp)
############## DO NOT TOUCH AREA: END ###################
