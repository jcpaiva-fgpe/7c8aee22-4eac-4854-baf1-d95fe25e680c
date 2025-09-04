import numpy as np
import json

def combined_emission(source1, source2):
    _source1 = np.array(source1)
    _source2 = np.array(source2)
    return (_source1 + _source2)


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input().strip()
    parts = inp.split(" ")
    source1 = json.loads(parts[0])
    source2 = json.loads(parts[1])
    print(combined_emission(source1, source2))
############## DO NOT TOUCH AREA: END ###################