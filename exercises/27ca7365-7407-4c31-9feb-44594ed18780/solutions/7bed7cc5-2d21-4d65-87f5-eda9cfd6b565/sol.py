import os
import numpy as np
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"
import matplotlib.pyplot as plt
    
def build_plot():
    # TODO this is what you need to complete
    doge_returns = np.random.normal(0, 5, 100)

    plt.boxplot(doge_returns)
    plt.title("Dogecoin Daily Returns")
    plt.ylabel("Return (%)")
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
