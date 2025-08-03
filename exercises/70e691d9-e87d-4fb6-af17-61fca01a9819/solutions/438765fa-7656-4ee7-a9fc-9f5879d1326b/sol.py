import numpy as np

def profits():
    # TODO this is what you need to complete
    btc = np.array([200, -300, 150])
    eth = np.array([-100, 250, 50])
    total = btc + eth
    return total


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    print(profits())
############## DO NOT TOUCH AREA: END ###################
