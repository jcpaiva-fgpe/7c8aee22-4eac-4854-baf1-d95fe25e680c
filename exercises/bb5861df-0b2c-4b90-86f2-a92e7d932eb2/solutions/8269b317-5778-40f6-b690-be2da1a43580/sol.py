import os
import numpy as np
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"
import matplotlib.pyplot as plt
    
def build_plot():
    # TODO this is what you need to complete
    btc_returns = np.random.normal(0, 1, 100)
    eth_returns = btc_returns * 0.8 + np.random.normal(0, 0.5, 100)

    plt.scatter(btc_returns, eth_returns)
    plt.title("BTC vs ETH Returns")
    plt.xlabel("BTC Returns")
    plt.ylabel("ETH Returns")
    plt.grid(True)
    

############## DO NOT TOUCH AREA: START #################
def save_boxplot():
    # Save plot
    file_path = 'boxplot_' + str(np.random.randint(1000)) + '.png'
    plt.savefig(file_path)
    plt.close()  # Close the figure to free memory
    return os.path.abspath(file_path)

def main():
    build_plot()
    path = save_boxplot()
    print(path)

if __name__ == '__main__':
    main()
############## DO NOT TOUCH AREA: END ###################
