/********************************************************
 *              DO NOT TOUCH AREA: START                *
 ********************************************************/

if __name__ == '__main__':
    entry = input()
    current = input()
    print(exercise(entry, current))

/********************************************************
 *                DO NOT TOUCH AREA: END                *
 ********************************************************/
    
def exercise(entry, current):
    # TODO this is what you need to complete
    gain = (current - entry) / entry * 100
    if gain > 50:
        return "SELL!"
    else:
        return "HODL"

    