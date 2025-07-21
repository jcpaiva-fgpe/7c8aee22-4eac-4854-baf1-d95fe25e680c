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
    anomalies = np.array([0.5, 0.7, 1.0, 1.2])
    return anomalies.mean(), anomalies.std(), anomalies.var()

    