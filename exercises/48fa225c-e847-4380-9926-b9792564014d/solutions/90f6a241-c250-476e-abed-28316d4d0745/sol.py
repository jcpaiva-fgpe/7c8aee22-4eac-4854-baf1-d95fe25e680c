import json

# TODO this is what you need to complete
def average_warming(cities):
    total = sum(cities.values())
    count = len(cities)
    return total / count


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    values = json.loads(inp)
    print(average_warming(values))
############## DO NOT TOUCH AREA: END ###################
