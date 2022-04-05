from datalib import parse_dataset
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
    data.display_data()