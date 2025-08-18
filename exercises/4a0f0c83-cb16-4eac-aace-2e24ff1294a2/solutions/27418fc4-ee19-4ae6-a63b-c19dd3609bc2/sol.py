import pandas as pd

def sort(path):
    # TODO this is what you need to complete
    sorted_df = df.sort_values(by="CO2", ascending=False)
    print(sorted_df)


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    result = sort(inp)
    print(result)
############## DO NOT TOUCH AREA: END ###################
