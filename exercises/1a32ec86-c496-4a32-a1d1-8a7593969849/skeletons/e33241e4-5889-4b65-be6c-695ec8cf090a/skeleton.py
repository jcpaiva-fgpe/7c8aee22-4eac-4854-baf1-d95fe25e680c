import os
import numpy as np
import pandas as pd
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"
import matplotlib.pyplot as plt
    
def build_plot(india_emissions):
    # TODO this is what you need to complete



############## DO NOT TOUCH AREA: START #################
def save_boxplot():
    # Save plot
    file_path = 'bar_climate_' + str(np.random.randint(1000)) + '.png'
    plt.savefig(file_path)
    plt.close()  # Close the figure to free memory
    return os.path.abspath(file_path)

if __name__ == '__main__':
    inp = input()
    df = pd.read_csv(inp)
    years = ['2040', '2041', '2042', '2043', '2044']
    india_data = df[df['country'] == 'India'].iloc[0]
    india_emissions = [india_data[year] for year in years]
    build_plot(india_emissions)
    path = save_boxplot()
    print(path)
############## DO NOT TOUCH AREA: END ###################
