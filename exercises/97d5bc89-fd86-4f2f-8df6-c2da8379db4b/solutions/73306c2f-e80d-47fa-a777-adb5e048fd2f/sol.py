import numpy as np
import json

def analyze(temperatures):
    # TODO this is what you need to complete
    anomalies = np.array(temperatures)
    mean = np.mean(anomalies)
    std_dev = np.std(anomalies)
    variance = np.var(anomalies)
    return mean, std_dev, variance


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    temperatures = json.loads(inp)
    mean, std_dev, variance = analyze(temperatures)
    print(mean, std_dev, variance)
############## DO NOT TOUCH AREA: END ###################
