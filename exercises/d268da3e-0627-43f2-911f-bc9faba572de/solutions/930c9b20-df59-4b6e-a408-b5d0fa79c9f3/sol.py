import pandas as pd

def explore(temperatures):
    # TODO this is what you need to complete
    df = pd.read_csv("emissions.csv")
    print(df.head())


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    explore(inp)
############## DO NOT TOUCH AREA: END ###################
