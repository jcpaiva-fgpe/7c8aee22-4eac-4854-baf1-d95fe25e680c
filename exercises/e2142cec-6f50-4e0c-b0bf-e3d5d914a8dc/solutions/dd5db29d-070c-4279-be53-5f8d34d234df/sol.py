import numpy as np

def reshape():
    # TODO this is what you need to complete
    profits = np.array([100, 150, -50, 200, -100, 80])
    trades = profits.reshape(2, 3)
    return trades


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    print(reshape())
############## DO NOT TOUCH AREA: END ###################
