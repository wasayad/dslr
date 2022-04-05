import sys
from tkinter import S
from datalib import parse_dataset
import numpy as np
import matplotlib.pyplot as plt


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
    note = []
    note.append(data.filter("Divination", 0))
    note.append(data.filter("History of Magic", 0))
    color = ['red']
    plt.scatter(range(len(note[0])), note[0], c=color, alpha=0.7, s=1.5)
    color = ['blue']
    plt.scatter(range(len(note[1])), note[1], c=color, alpha=0.7, s=1.5)
    plt.show()