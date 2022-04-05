import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import S
from datalib import parse_dataset
import numpy as np
import matplotlib.pyplot as plt
import sys


if __name__ == '__main__':
    data = parse_dataset()
    if (len(sys.argv) != 2):
        sys.exit("Error: argument number is invalid.")
    data.get_data(sys.argv[1])
    data.get_nb_features()
    data.get_mean()
    data.get_min()
    data.get_max()
    data.get_lower_quartil()
    data.get_median()
    data.get_upper_quartil()
    data.get_std()

    data.convert()
    note = {}
    for index, row in enumerate(data.features_name):
        if (index > 0):
            note[row] = []
            for i in range(len(data.data)):
                note[row].append(data.data[i][index])
    note = pd.DataFrame(note)

    sns.set_style('darkgrid')
    sns.pairplot(note, hue="Hogwarts House", )
    plt.savefig("test.png")
