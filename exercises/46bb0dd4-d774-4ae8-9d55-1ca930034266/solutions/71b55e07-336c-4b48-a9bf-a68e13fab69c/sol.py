import numpy as np

/********************************************************
 *              DO NOT TOUCH AREA: START                *
 ********************************************************/

if __name__ == '__main__':
    array1 = input()
    array2 = input()
    print(exercise(array1, array2))

/********************************************************
 *                DO NOT TOUCH AREA: END                *
 ********************************************************/
    
def exercise(array1, array2):
    co2 = np.array(array1)
    ch4 = np.array(array2)
    return co2 + ch4

    