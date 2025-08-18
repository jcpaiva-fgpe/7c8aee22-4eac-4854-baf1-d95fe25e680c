import pandas as pd

def dataframe(path):
    # TODO this is what you need to complete
    df = pd.read_csv("portfolio.csv")
    print(df.head())


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    result = dataframe(inp)
############## DO NOT TOUCH AREA: END ###################
