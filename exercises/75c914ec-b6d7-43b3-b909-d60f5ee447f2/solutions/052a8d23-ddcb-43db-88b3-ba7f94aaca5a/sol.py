import numpy as np

/********************************************************
 *              DO NOT TOUCH AREA: START                *
 ********************************************************/

if __name__ == '__main__':
    array = input()
    print(exercise(array))

/********************************************************
 *                DO NOT TOUCH AREA: END                *
 ********************************************************/
    
def exercise(array):
    readings = np.array(array)
    matrix = readings.reshape(2, 3)
    return matrix

    