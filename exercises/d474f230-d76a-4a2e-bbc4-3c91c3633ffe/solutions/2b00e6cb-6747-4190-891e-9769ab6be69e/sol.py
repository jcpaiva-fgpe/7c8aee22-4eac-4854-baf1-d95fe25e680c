import numpy as np

def greenhouse_levels(co2_levels, methane_levels):
    # TODO this is what you need to complete
    _co2_levels = np.array(co2)
    _methane_levels = np.array(methane)
    return np.add(_co2_levels, _methane_levels)


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    co2_levels = inp.slit(" ")[0]
    methane_levels = inp.slit(" ")[1]
    print(greenhouse_levels(co2_levels, methane_levels))
############## DO NOT TOUCH AREA: END ###################
