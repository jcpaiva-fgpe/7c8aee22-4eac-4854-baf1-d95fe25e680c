import numpy as np

def co2():
    # TODO this is what you need to complete
    readings = np.array([600, 550, 680, 700, 720, 650])
    reshaped = readings.reshape(2, 3)
    return reshaped


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    print(co2())
############## DO NOT TOUCH AREA: END ###################
