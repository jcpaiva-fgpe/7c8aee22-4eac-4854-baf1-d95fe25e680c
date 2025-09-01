import numpy as np
import json

def greenhouse_levels(co2_levels, methane_levels):
    _co2_levels = np.array(co2_levels)
    _methane_levels = np.array(methane_levels)
    return (_co2_levels + _methane_levels)


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input().strip()
    parts = inp.split(" ")
    co2_levels = json.loads(parts[0])
    methane_levels = json.loads(parts[1])
    print(greenhouse_levels(co2_levels, methane_levels))
############## DO NOT TOUCH AREA: END ###################