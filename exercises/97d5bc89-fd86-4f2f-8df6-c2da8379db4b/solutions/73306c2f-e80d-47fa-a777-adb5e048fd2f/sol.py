import numpy as np
import json

def analyze(warmings):
    # TODO this is what you need to complete
    anomalies = np.array(warmings)
    mean = np.mean(anomalies)
    std_dev = np.std(anomalies)
    variance = np.var(anomalies)
    return mean, std_dev, variance


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    warmings = json.loads(inp)
    mean, std_dev, variance = analyze(warmings)
    print(mean, std_dev, variance)
############## DO NOT TOUCH AREA: END ###################
