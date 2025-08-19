import pandas as pd

def average(path):
    # TODO this is what you need to complete
    mean_co2 = df["CO2"].mean()
    print("Average CO₂:", mean_co2)


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    result = average(inp)
    print(result)
############## DO NOT TOUCH AREA: END ###################
