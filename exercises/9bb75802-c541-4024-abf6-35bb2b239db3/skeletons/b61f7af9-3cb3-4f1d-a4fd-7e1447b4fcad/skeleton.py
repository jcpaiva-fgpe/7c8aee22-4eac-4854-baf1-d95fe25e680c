import os
import numpy as np
import pandas as pd
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"
import matplotlib.pyplot as plt
    
def build_plot(path):
    # TODO this is what you need to complete

    

############## DO NOT TOUCH AREA: START #################
def save_boxplot():
    # Save plot
    file_path = 'mlplot_' + str(np.random.randint(1000)) + '.png'
    plt.savefig(file_path)
    plt.close()  # Close the figure to free memory
    return os.path.abspath(file_path)

if __name__ == '__main__':
    inp = input()
    build_plot(path)
    path = save_boxplot()
    print(path)
############## DO NOT TOUCH AREA: END ###################
