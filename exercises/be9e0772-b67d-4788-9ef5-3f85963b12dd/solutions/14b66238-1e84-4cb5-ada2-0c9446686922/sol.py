import json
# TODO this is what you need to complete
def portfolio(coins):
    total = 0
    for price in coins.values():
        total += price
    return total


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    data = json.loads(inp)
    print(portfolio(data))
############## DO NOT TOUCH AREA: END ###################
