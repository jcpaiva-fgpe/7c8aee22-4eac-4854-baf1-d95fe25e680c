import numpy as np

def co2():
    # TODO this is what you need to complete
    readings = np.array([0.9, 1.1, 1.3, 0.7, 1.0, 1.2])
    reshaped = readings.reshape(2, 3)
    return reshaped


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    print(co2())
############## DO NOT TOUCH AREA: END ###################
