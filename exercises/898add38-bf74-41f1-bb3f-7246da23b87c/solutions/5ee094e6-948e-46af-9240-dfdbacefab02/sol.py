import json

def check(sweeps):
    # TODO this is what you need to complete
    result_parts = []
    for i in range(len(sweeps)):
        result_parts.append(f"Exchange {i+1}: {sweeps[i]} BTC")
    result = ", ".join(result_parts)
    print(result)


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    sweeps = json.loads(inp)
    check(sweeps)
############## DO NOT TOUCH AREA: END ###################
