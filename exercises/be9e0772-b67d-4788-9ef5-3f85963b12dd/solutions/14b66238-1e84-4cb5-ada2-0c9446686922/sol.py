import json
# TODO this is what you need to complete
def average(coins):
    total = 0
    for price in coins.values():
        total += price
    avg = total / len(coins)
    return round(avg, 1)


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    data = json.loads(inp)
    print(average(data))
############## DO NOT TOUCH AREA: END ###################
