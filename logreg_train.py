import sys
from numpy import NaN
from datalib import parse_dataset
import math

class train_gryffindor:
    def __init__(self):
        self.theta1 = 1
        self.theta2 = 1
        self.theta3 = 1
        self.theta4 = 1
        self.data = []
    def set_data(self, data, house, index1, index2):
        for row in data.data:
           if (row[1] == house):
               if (row[index1] == ""):
                   self.data.append([1, float(data.features["mean"][index2])/ 1000])
               else:
                   self.data.append([1, float(row[index1])/ 1000])
           else:
               if (row[index1] == ""):
                   self.data.append([0, float(data.features["mean"][index2])/ 1000])
               else:
                   self.data.append([0, float(row[index1])/ 1000])

    def logistic_function(self, x, theta):
        return (1 / (1 + math.exp(-(theta * x))))
    def sigma(self, data, theta):
        sum = 0
        for i in data:
            sum += (self.logistic_function(i[1], theta) - i[0]) * i[1]
        return sum
    def cost_function1(self):
        self.theta1 -= 1 / len(self.data) * self.sigma(self.data, self.theta1)
    def cost_function2(self):
        self.theta2 -= 1 / len(self.data) * self.sigma(self.data, self.theta2)
    def cost_function3(self):
        self.theta3 -= 1 / len(self.data) * self.sigma(self.data, self.theta3)
    def cost_function4(self):
        self.theta4 -= 1 / len(self.data) * self.sigma(self.data, self.theta4)        

        
        

test = train_gryffindor()
data = parse_dataset()
data.get_data(sys.argv[1])
data.get_nb_features()
data.get_mean()

test.set_data(data, "Gryffindor", 18, 12)

for i in range(1000):
    test.cost_function1()
    
test.set_data(data, "Ravenclaw", 11, 5)
for i in range(1000):
    test.cost_function2()

test.set_data(data, "Slytherin", 10, 4)
for i in range(1000):
    test.cost_function3()

test.set_data(data, "Hufflepuff", 17, 11)
for i in range(1000):
    test.cost_function4()
print(data.data[365][1])
print(test.logistic_function(float(data.data[365][18]) / 1000, test.theta1))
print(test.logistic_function(float(data.data[365][11]) / 1000, test.theta2))
print(test.logistic_function(float(data.data[365][10]) / 1000, test.theta3))
print(test.logistic_function(float(data.data[365][17]) / 1000, test.theta4))

who = []
result = []
compare = []
for row in data.data:
    if (row[11] != "" and row[10] != "" and row[17] != "" and row[18] != "" and row[1] != "Hufflepuff"):
        who = [test.logistic_function(float(row[18]) / 1000, test.theta1), test.logistic_function(float(row[11]) / 1000, test.theta2), test.logistic_function(float(row[10]) / 1000, test.theta3), test.logistic_function( float(row[17]) / 1000, test.theta4)]
        compare.append(row[1])
        if (who[0] > who[1] and who[0] > who[2] and who[0] > who[3]):
            print(who)
            print("Gryddindor = ", row[1])
            result.append("Gryffindor")
        elif (who[1] > who[0] and who[1] > who[2] and who[1] > who[3]):
            print("Ravenclaw = ", row[1])
            result.append("Ravenclaw")
        elif (who[2] > who[0] and who[2] > who[1] and who[2] > who[3]):
            print("Slytherin = ", row[1])
            result.append("Slytherin")
        elif (who[3] > who[0] and who[3] > who[1] and who[3] > who[2]):
            print("Hufflepuff = ", row[1])
            result.append("Hufflepuff")
j = 0         
for index, i in enumerate(compare):
    if (result[index] == i):
        j+= 1
print(len(compare), len(result))
print("Accuracy =", j * 100 / len(compare), "%")