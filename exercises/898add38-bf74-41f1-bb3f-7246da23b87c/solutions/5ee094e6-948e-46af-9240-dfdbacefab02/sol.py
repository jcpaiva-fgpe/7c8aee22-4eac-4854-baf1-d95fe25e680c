import json

def check(wallet):
    # TODO this is what you need to complete
    result = ""
    for i in range(len(wallet)):
        if i == 0:
            result += wallet[i]
        else:
            result += ", " + wallet[i]
    print(result)


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    wallet = json.loads(inp)
    check(wallet)
############## DO NOT TOUCH AREA: END ###################
