import numpy as np

/********************************************************
 *              DO NOT TOUCH AREA: START                *
 ********************************************************/

if __name__ == '__main__':
    seed = input
    print(exercise(seed))

/********************************************************
 *                DO NOT TOUCH AREA: END                *
 ********************************************************/
    
def exercise(seed):
    anomaly_sim = np.random.normal(loc=1.0, scale=0.2, size=1000)
    return anomaly_sim[:5]

    