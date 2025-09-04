import os
import numpy as np
import pandas as pd
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"
import matplotlib.pyplot as plt
    
def build_plot(avg_close):
    # TODO this is what you need to complete

    

############## DO NOT TOUCH AREA: START #################
def save_boxplot():
    # Save plot
    file_path = 'barplot_' + str(np.random.randint(1000)) + '.png'
    plt.savefig(file_path)
    plt.close()  # Close the figure to free memory
    return os.path.abspath(file_path)

if __name__ == '__main__':
    inp = input()
    df = pd.read_csv(inp)
    avg_prices = df.groupby('Name')['Close'].mean()
    avg_close = [avg_prices['Bitcoin'], avg_prices['Ethereum']]
    build_plot(avg_close)
    path = save_boxplot()
    print(path)
############## DO NOT TOUCH AREA: END ###################
