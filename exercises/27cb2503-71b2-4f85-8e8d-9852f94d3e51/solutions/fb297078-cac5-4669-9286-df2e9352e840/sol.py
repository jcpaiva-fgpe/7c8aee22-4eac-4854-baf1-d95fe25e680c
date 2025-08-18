import os
import numpy as np
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"
import matplotlib.pyplot as plt
    
def build_plot():
    # TODO this is what you need to complete
    plt.plot(days, btc_prices, color='green', linestyle='--', marker='o')
    plt.title("Bitcoin Price Over 30 Days", fontsize=14, color='blue')
    plt.xlabel("Day")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.annotate("Start", xy=(1, btc_prices[0]), xytext=(3, btc_prices[0]+500),
                arrowprops=dict(facecolor='black', shrink=0.05))
    

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
