import sys
from numpy import NaN
from datalib import parse_dataset
import math

class train:
    def __init__(self):
        self.theta = 1
        self.data = []
        
    def logistic_function(self, x):
        return (1 / (1 + math.exp(-(self.theta * x))))
    def sigma(self, data):
        sum = 0
        for i in data:
            sum += (self.logistic_function(i[1]) - i[0]) * i[1]
        print(sum)
        return sum
    def cost_function(self):
        print("Theta = ",self.theta)
        self.theta -= 1 / len(self.data) * self.sigma(self.data)
        pass
        
        
        

test = train()
data = parse_dataset()
data.get_data(sys.argv[1])
data.get_nb_features()
data.get_mean()
for row in data.data:
    if (row[1] == "Gryffindor"):
        if (row[18] == ""):
            test.data.append([1, float(data.features["mean"][12])])
        else:
            test.data.append([1, float(row[18])])
    else:
        if (row[18] == ""):
            print("hey")
            test.data.append([0, float(data.features["mean"][12])])
        else:
            test.data.append([0, float(row[18])])
for i in range(2):
    test.cost_function()
    
