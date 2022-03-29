import sys

class dataset:
    def __init__(self):
        self.data = []
        self.nb_feature = 0
        self.mean = []
        self.std = 0
        self.min = 0
        self.quarter = 0
        self.half = 0
        self.three_quarter = 0
        self.max = 0
    def get_data(self, path):
        try:
            with open(path, "r") as f:
                for index, row in enumerate(f):
                    if (index != 0):
                        self.data.append(row.split(','))
        except:
            sys.exit("Error: dataset invalid.")
    def get_mean(self):
        for index, row in enumerate(self.data):
            for column in self.data:
                try:
                    print(float(column[index]))
                except:
                    break
    def get_nb_features(self):
        for row in self.data[0]:
            try:
                float(row)
                self.nb_feature += 1
            except:
                continue

if __name__ == '__main__':
    data = dataset()
    if (len(sys.argv) != 2):
        sys.exit("Error: argument number is invalid.")
    data.get_data(sys.argv[1])
    data.get_nb_features()
    print(data.nb_feature)
    #data.get_mean()