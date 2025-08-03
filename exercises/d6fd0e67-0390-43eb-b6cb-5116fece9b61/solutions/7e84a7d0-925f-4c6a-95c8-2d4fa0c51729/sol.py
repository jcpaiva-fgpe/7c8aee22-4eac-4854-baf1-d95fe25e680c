import json
import numpy as np

def stats(array):
    # TODO this is what you need to complete
    gains = np.array(array)
    mean = gains.mean()
    std = gains.std()
    maximum = gains.max()
    return mean, std, maximum


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    array = json.loads(inp)
    mean, std, maximum = stats(array)
    print(mean, std, maximum)
############## DO NOT TOUCH AREA: END ###################
