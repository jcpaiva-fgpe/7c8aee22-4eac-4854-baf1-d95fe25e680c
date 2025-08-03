def decide(temp_rise):
    # TODO this is what you need to complete
    if temp_rise > 1.5:
        print("Danger")
    else:
        print("Within limits")


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    temp_rise = float(inp)
    decide(temp_rise)
############## DO NOT TOUCH AREA: END ###################
