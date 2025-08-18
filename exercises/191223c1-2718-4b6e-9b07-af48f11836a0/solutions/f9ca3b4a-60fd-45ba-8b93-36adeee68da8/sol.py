import os
import numpy as np
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"
import matplotlib.pyplot as plt
    
def build_plot():
    # TODO this is what you need to complete
    days = list(range(1, 31))
    prices = np.random.normal(65000, 2000, 30)
    plt.plot(days, prices)
    plt.title("BTC Price - Last 30 Days")
    plt.xlabel("Day")
    plt.ylabel("Price ($)")
    

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
