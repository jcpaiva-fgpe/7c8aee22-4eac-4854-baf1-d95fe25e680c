import pandas as pd

def scaling(path):
    # TODO this is what you need to complete
    df["CO2_scaled"] = df["CO2"].apply(lambda x: x / 10)
    print(df[["CO2", "CO2_scaled"]].head())


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    result = scaling(inp)
    print(result)
############## DO NOT TOUCH AREA: END ###################
