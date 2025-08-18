import pandas as pd

def summarize(path):
    # TODO this is what you need to complete
    grouped = df.groupby("Category")["Value"].sum()
    print(grouped)


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    summarize(inp)
############## DO NOT TOUCH AREA: END ###################
