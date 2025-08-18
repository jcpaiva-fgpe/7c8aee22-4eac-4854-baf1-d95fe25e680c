import pandas as pd

def filtering(path):
    # TODO this is what you need to complete
    profitable = df[df["CurrentPrice"] > df["BuyPrice"]]
    return profitable


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    result = filtering(inp)
    print(result)
############## DO NOT TOUCH AREA: END ###################
