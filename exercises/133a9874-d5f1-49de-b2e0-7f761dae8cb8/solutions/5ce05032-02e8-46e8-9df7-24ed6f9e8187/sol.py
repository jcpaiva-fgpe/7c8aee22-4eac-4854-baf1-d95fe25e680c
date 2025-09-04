def sell_or_not(price_change):
    # TODO this is what you need to complete
    if price_change > 5000:
        print("Alert: High volatility")
    else:
        print("Stable")


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    price_change = int(inp)
    sell_or_not(price_change)
############## DO NOT TOUCH AREA: END ###################
