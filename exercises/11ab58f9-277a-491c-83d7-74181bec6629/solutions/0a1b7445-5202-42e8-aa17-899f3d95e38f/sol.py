import pandas as pd

def average(path):
    # TODO this is what you need to complete
    df = pd.read_csv(path)
    mean_co2 = df["2040"].mean()
    return mean_co2


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    mean = average(inp)
    print(mean)
############## DO NOT TOUCH AREA: END ###################
