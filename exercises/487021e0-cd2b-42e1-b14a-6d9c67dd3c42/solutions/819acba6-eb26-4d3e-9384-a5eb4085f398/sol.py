/********************************************************
 *              DO NOT TOUCH AREA: START                *
 ********************************************************/

if __name__ == '__main__':
    portfolio = input()
    coin = input()
    print(time_to_buy(portfolio, coin))

/********************************************************
 *                DO NOT TOUCH AREA: END                *
 ********************************************************/
    
def time_to_buy(portfolio, coin):
    if coin in portfolio:
        return portfolio[coin] < 2
    else:
        return True

    