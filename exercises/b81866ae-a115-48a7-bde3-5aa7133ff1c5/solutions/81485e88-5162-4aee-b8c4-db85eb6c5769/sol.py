/********************************************************
 *              DO NOT TOUCH AREA: START                *
 ********************************************************/

if __name__ == '__main__':
    wallet = input()
    print(portfolio_summary(wallet))

/********************************************************
 *                DO NOT TOUCH AREA: END                *
 ********************************************************/
    
def portfolio_summary(wallet):
    summary = []
    for coin, amount in wallet.items():
        summary.append(f"{coin}: {amount}")
    return summary
    