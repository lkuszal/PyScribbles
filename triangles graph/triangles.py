import numpy as np


class Triangle:
    def __init__(self, path):
        file = open(path, "r")
        matr_list = []
        for line in file.readlines():
            matr_list.append(line.split())
        matrix = np.zeros((len(matr_list), len(matr_list)), dtype="i")
        for y in range(len(matr_list)):
            for x in range(len(matr_list[y])):
                matrix[y, x] = int(matr_list[y][x])
        self.matrix = matrix
        self.length = len(matr_list)
        self.results = {}
    
    def finding(self):
        self.find_the_way(0, 0, str(self.length), self.length)
    
    def find_the_way(self, level, index, path, sum):
        if level == self.length - 1:
            if sum in self.results.keys():
                self.results[sum].append(path)
            else:
                self.results[sum] = [path]
        else:
            new_level = level + 1
            for i in [0, 1]:
                new_index = index + i
                new_element = self.matrix[new_level, new_index]
                new_path = path + str(new_element)
                new_sum = sum + new_element
                self.find_the_way(new_level, new_index, new_path, new_sum)
    
    def answer(self):
        sums = list(self.results.keys())
        sums.sort()
        self.maxsum = sums[-1]
        self.maxpaths = self.results[sums[-1]]


for x in range(1, 4):
    obj = Triangle(str(x) + ".txt")
    obj.finding()
    obj.answer()
    print(obj.maxsum, obj.maxpaths)




