import sys
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

    fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2)
    data.convert()
    ax0.hist(data.filter("Care of Magical Creatures", 0, data.filter("Hogwarts House", "Ravenclaw")),  color='blue', alpha=0.5   , density=1)
    ax0.hist(data.filter("Care of Magical Creatures", 0, data.filter("Hogwarts House", "Gryffindor")), color='red', alpha=0.5   , density=1 )
    ax0.hist(data.filter("Care of Magical Creatures", 0, data.filter("Hogwarts House", "Slytherin")),  color='green', alpha=0.5  , density=1)
    ax0.hist(data.filter("Care of Magical Creatures", 0, data.filter("Hogwarts House", "Hufflepuff")), color='yellow', alpha=0.5, density=1 )
    ax0.legend(prop={'size': 0.5})
    ax0.set_title('Histogram')
    ax0.legend(["Ravenclaw", "Gryffindor", "Slytherin", "Hufflepuff"])
    ax1.hist(data.filter("Arithmancy", 0, data.filter("Hogwarts House", "Ravenclaw")),  color='blue', alpha=0.5   , density=1)
    ax1.hist(data.filter("Arithmancy", 0, data.filter("Hogwarts House", "Gryffindor")), color='red', alpha=0.5   , density=1 )
    ax1.hist(data.filter("Arithmancy", 0, data.filter("Hogwarts House", "Slytherin")),  color='green', alpha=0.5  , density=1)
    ax1.hist(data.filter("Arithmancy", 0, data.filter("Hogwarts House", "Hufflepuff")), color='yellow', alpha=0.5, density=1 )
    ax1.legend(prop={'size': 0.5})
    ax1.set_title('Histogram')
    ax1.legend(["Ravenclaw", "Gryffindor", "Slytherin", "Hufflepuff"])
    plt.show()