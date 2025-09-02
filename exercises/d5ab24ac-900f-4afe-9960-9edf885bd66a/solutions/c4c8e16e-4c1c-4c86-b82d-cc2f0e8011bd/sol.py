import os
import numpy as np
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"
import matplotlib.pyplot as plt
    
def build_plot():
    # TODO this is what you need to complete
    plt.pie(volume_share.values, labels=volume_share.index)

    

############## DO NOT TOUCH AREA: START #################
def save_boxplot():
    # Save plot
    file_path = 'boxplot_' + str(np.random.randint(1000)) + '.png'
    plt.savefig(file_path)
    plt.close()  # Close the figure to free memory
    return os.path.abspath(file_path)

if __name__ == '__main__':
    inp = input()
    df = pd.read_csv(inp)
    volume_share = df.groupby('Name')['Volume'].sum()
    build_plot(volume_share)
    path = save_boxplot()
    print(path)
############## DO NOT TOUCH AREA: END ###################
