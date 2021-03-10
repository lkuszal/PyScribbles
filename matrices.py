import numpy as np
import random
import time


def czytaj(nazwa):
    with open(nazwa) as f:
        dane = f.readlines()
    n = len(dane)
    a = np.zeros((n, n), 'd')
    b = np.zeros((n,))
    i = 0
    for x in dane:
        x = x.split()
        for j in range(n):
            a[i, j] = float(x[j])
        b[i] = float(x[n])
        i += 1
    return a, b


def iszero(a):
    a = np.nan_to_num(a)
    if abs(a) < 2.0e-12:
        return True
    else:
        return False


def czyGTr(matrix):
    matrix = matrix.copy()
    if matrix.shape[0] != matrix.shape[1]:
        return False
    for y in range(1, matrix.shape[0]):
        for x in range(y):
            if not iszero(matrix[y, x]):
                return False
    return True


def rozwUGTr(matrix, arr):
    matrix = matrix.copy()
    arr = arr.copy()
    if not czyGTr(matrix):
        return -1
    solution = np.zeros(matrix.shape[0])
    for y in range(matrix.shape[0] - 1, -1, -1):
        if iszero(matrix[y, y]):
            return -1
        for x in range(matrix.shape[0] - 1, y, -1):
            arr[y] -= solution[x] * matrix[y, x]
        solution[y] = arr[y] / matrix[y, y]
    return solution


def basicGauss(matrix, arr):
    matrix = matrix.copy()
    arr = arr.copy()
    if len({matrix.shape[0], matrix.shape[1], arr.shape[0]}) > 1:
        return -1, -1
    for x1 in range(matrix.shape[0]-1):
        if iszero(matrix[x1, x1]):
            return -1, -1
        for y in range(x1 + 1, matrix.shape[0]):
            mult = matrix[y, x1] / matrix[x1, x1]
            for x2 in range(x1, matrix.shape[0]):
                matrix[y, x2] -= mult * matrix[x1, x2]
            arr[y] -= mult * arr[x1]
    return matrix, arr


def nonzeroGauss(matrix, arr):
    matrix = matrix.copy()
    arr = arr.copy()
    if len({matrix.shape[0], matrix.shape[1], arr.shape[0]}) > 1:
        return -1, -1
    for x1 in range(matrix.shape[0]-1):
        if iszero(matrix[x1, x1]):
            switched = False
            for yn in range(x1 + 1, matrix.shape[0]):
                if not iszero(matrix[yn, x1]):
                    matrix[[x1, yn]] = matrix[[yn, x1]]
                    arr[[x1, yn]] = arr[[yn, x1]]
                    switched = True
                    break
            if not switched:
                return -1, -1
        for y in range(x1 + 1, matrix.shape[0]):
            mult = matrix[y, x1] / matrix[x1, x1]
            for x2 in range(x1, matrix.shape[0]):
                matrix[y, x2] -= mult * matrix[x1, x2]
            arr[y] -= mult * arr[x1]
    return matrix, arr


def numericGauss(matrix, arr):
    matrix = matrix.copy()
    arr = arr.copy()
    if len({matrix.shape[0], matrix.shape[1], arr.shape[0]}) > 1:
        return -1, -1
    for x1 in range(matrix.shape[0]-1):
        maxind = x1
        maxval = matrix[x1, x1]
        for yn in range(x1 + 1, matrix.shape[0]):
            if matrix[yn, x1] > maxval:
                maxind = yn
                maxval = matrix[yn, x1]
        if iszero(maxval):
            return -1, -1
        matrix[[x1, maxind]] = matrix[[maxind, x1]]
        arr[[x1, maxind]] = arr[[maxind, x1]]
        for y in range(x1 + 1, matrix.shape[0]):
            mult = matrix[y, x1] / matrix[x1, x1]
            for x2 in range(x1, matrix.shape[0]):
                matrix[y, x2] -= mult * matrix[x1, x2]
            arr[y] -= mult * arr[x1]
    return matrix, arr


def solver(matrix, arr, func):
    print(func.__name__)
    matrix = matrix.copy()
    arr = arr.copy()
    t1 = time.perf_counter()
    a, b = func(matrix, arr)
    if type(a) == int:
        print("Nieudane przeksztalcenie Gaussa")
        print(0)
        return -1
    t2 = time.perf_counter()
    sol1 = rozwUGTr(a, b)
    if type(sol1) == int:
        print("Nieudane rozwiazanie")
        print(0)
        return -1
    sol2 = np.linalg.solve(matrix, arr)
    diffs = abs(sol1 - sol2)
    diffs.sort()
    print(diffs[-1])
    print(round(t2 - t1, 6))
    return 0


def compar(matrix, arr):
    solver(matrix, arr, basicGauss)
    solver(matrix, arr, nonzeroGauss)
    solver(matrix, arr, numericGauss)
    print("Rozwiazanie")
    wynik=abs(np.linalg.solve(matrix, arr))
    wynik.sort()
    print(wynik[0])


#macierz = 'h8'
#a, b = czytaj(macierz)

#compar(a, b)

n=300
print(n)
a=np.random.rand(n,n)
for x in range(n):
    a[x,x]+=1
b=np.random.rand(n)
compar(a,b)