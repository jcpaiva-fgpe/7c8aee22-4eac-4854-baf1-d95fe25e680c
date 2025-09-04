import numpy as np

def profits(bitcoin, ethereum):
    # TODO this is what you need to complete
    btc = np.array(bitcoin)
    eth = np.array(ethereum)
    total = btc + eth
    return total


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input().strip()
    parts = inp.split(" ")
    bitcoin = json.loads(parts[0])
    ethereum = json.loads(parts[1])
    print(profits(bitcoin, ethereum))
############## DO NOT TOUCH AREA: END ###################
