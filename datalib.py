import sys

from numpy import NaN

class parse_dataset:
    def __init__(self):
        self.data = []
        self.nb_feature = []
        self.features = {"count": [], "mean": [], "std": [],
                         "min": [], "q1": [], "q2": [], "q3": [], "max": []}
        self.summary = {}
        self.features_name = []
    def sqrt(self, nb):
        i = 1
        if (nb < 0):
            i = -1
            nb *= i
        nb = nb ** 0.5
        return nb

    def get_data(self, path):
        try:
            with open(path, "r") as f:
                for index, row in enumerate(f):
                    if (index != 0):
                        self.data.append(row.split(','))
                    else:
                        for i, column in enumerate(row.split(',')):
                            column = column.replace("\n", "")
                            self.summary[column] = i
                            self.features_name.append(column)
        except:
            sys.exit("Error: dataset invalid.")

    def get_mean(self):
        i = 0
        for index in range(len(self.nb_feature)):
            self.features["mean"].append(0)
            for column in range(len(self.data)):
                try:
                    self.features["mean"][index] += float(
                        self.data[column][self.nb_feature[index]])
                except:
                    i += 1
                    continue
            self.features["mean"][index] /= (len(self.data) - i)

    def get_std(self):
        i = 0
        for index in range(len(self.nb_feature)):
            self.features["std"].append(0)
            for column in range(len(self.data)):
                try:
                    self.features["std"][index] += (float(
                        self.data[column][self.nb_feature[index]]) - self.features["mean"][index]) ** 2
                except:
                    i += 1
                    continue
            self.features["std"][index] = self.sqrt(
                self.features["std"][index] / (len(self.data) - i))

    def get_min(self, data = []):
        for index in range(len(self.nb_feature)):
            min = []
            self.features["min"].append(0)
            for column in range(len(self.data)):
                try:
                    min.append(float(self.data[column][self.nb_feature[index]]))
                except:
                    continue
            self.features["min"][index] = sorted(min)[0]

    def get_max(self, data = []):
        if (data == []):
            for index in range(len(self.nb_feature)):
                max = []
                self.features["max"].append(0)
                for column in range(len(self.data)):
                    try:
                        max.append(
                            float(self.data[column][self.nb_feature[index]]))
                    except:
                        continue
                self.features["max"][index] = sorted(max)[len(max) - 1]
        else:
            max = []
            for row in data:
                try:
                    max.append(float(row))
                except:
                    continue
            return sorted(max)[len(max) - 1]

    def get_lower_quartil(self):
        for index in range(len(self.nb_feature)):
            q1 = []
            i = 0
            self.features["q1"].append(0)
            for column in range(len(self.data)):
                try:
                    q1.append(float(self.data[column][self.nb_feature[index]]))
                except:
                    i += 1
                    continue
            self.features["q1"][index] = sorted(
                q1)[int((len(q1) - 1 - i) * 0.25)]

    def get_median(self):
        for index in range(len(self.nb_feature)):
            q2 = []
            i = 0
            self.features["q2"].append(0)
            for column in range(len(self.data)):
                try:
                    q2.append(float(self.data[column][self.nb_feature[index]]))
                except:
                    i += 1
                    continue
            self.features["q2"][index] = sorted(
                q2)[int((len(q2) - 1 - i) * 0.5)]

    def get_upper_quartil(self):
        for index in range(len(self.nb_feature)):
            q3 = []
            i = 0
            self.features["q3"].append(0)
            for column in range(len(self.data)):
                try:
                    q3.append(float(self.data[column][self.nb_feature[index]]))
                except:
                    i += 1
                    continue
            self.features["q3"][index] = sorted(
                q3)[int((len(q3) - 1 - i) * 0.75)]

    def get_nb_features(self):
        for index, row in enumerate(self.data[0]):
            if (index != 0):
                try:
                    if (row != ""):
                        float(row)
                    self.nb_feature.append(index)
                except:
                    continue

    def get_len(self):
        for i in range(len(self.nb_feature)):
            j = 0
            for index in range(len(self.data)):
                if (self.data[index][self.nb_feature[i]] == ""):
                    j += 1
            self.features["count"].append(len(self.data) - j)
    def display_data(self):
        formated_str = []
        self.get_len()
        for i in range(len(self.features) + 1):
            formated_str.append("")
        formated_str[0] += "{:>8}".format("")
        for i in range(len(self.nb_feature)):
            formated_str[0] += "{:>{}s}".format(self.features_name[self.nb_feature[i]], int(len(self.features_name[self.nb_feature[i]]) * 1.5))
        print(formated_str[0])
        for index, keys in enumerate(self.features.keys()):
            formated_str[index + 1] = "{:<8s}".format(keys)
            for i, value in enumerate(self.features[keys]):
                formated_str[index + 1] += "{:>{}.2f}".format(value, int(len(self.features_name[self.nb_feature[i]]) * 1.5))
            print(formated_str[index + 1])
    def filter(self, column, filter = 0, data=[]):
        ret = []
        try:
            if (data == []):
                if (filter == 0):
                    for row in self.data:
                        ret.append(row[self.summary[column]])
                else:
                    for row in self.data:
                        if (row[self.summary[column]] == filter):
                            ret.append(row)
            else:
                if (filter == 0):
                    for row in data:
                        ret.append(row[self.summary[column]])
                else:
                    for row in data:
                        if (row[self.summary[column]] == filter):
                            ret.append(row)
        except:
            sys.exit("Error: filter function.")
        return ret

    def convert(self):
        for i in self.nb_feature:
            for index, row in enumerate(self.data):
                try:
                    if (self.data[index][i] == ""):
                        self.data[index][i] = NaN
                    else:
                        self.data[index][i] = float(row[i])
                except:
                    continue
    
    def get_custom_mean(self, data, column = ""):
        try:
            sum = 0
            i = 0
            if (column == ""):
                for row in data():
                    try:
                        sum += float(row)
                    except:
                        i += 1
                sum /= len(data) - i
            else:
                for row in data:
                    try:
                        sum += float(row[self.summary[column]])
                    except:
                        i += 1
                sum /= len(data) - i
        except:
            sys.exit("Error: function get_custom_mean")
        return sum

    def get_custom_std(self, data, column = ""):
        mean = self.get_custom_mean(data, column)
        try:
            sum = 0
            i = 0
            if (column == ""):
                for row in data():
                    try:
                        sum += (float(row) - mean) ** 2
                    except:
                        i += 1
                sum = self.sqrt()
            else:
                for row in data:
                    try:
                        sum += float(row[self.summary[column]])
                    except:
                        i += 1
                sum /= len(data) - i
        except:
            sys.exit("Error: function get_custom_mean")
        return sum

    def get_percent(self, data, column = ""):
        try:
            max = 0
            for index, name in enumerate(self.features_name):
                if(column == name):
                    max = self.features["max"][index - (len(self.data[0]) - len(self.nb_feature))] - self.features["min"][index - (len(self.data[0]) - len(self.nb_feature))]
            for row in data:
                try:
                    row = int(row * 100 / max)
                except:
                    continue
        except:
            sys.exit("Error: normalise function.")
        return data
            