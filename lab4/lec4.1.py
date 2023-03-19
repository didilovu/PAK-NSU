import numpy as np
import random

np.random.seed(18182)

f= open('B:\ile_1.txt')
data1 = np.array(f.read().split(' '))
f.close()
data1 = data1.astype(int)
print(data1)

g = open('B:\ile_2.txt')
data2 = np.array(g.read().split(' '))
g.close()
data2 = data2.astype(int)
print(data2)

P= float(input('P = '))

b = np.random.rand(1, len(data1))
print(b)
b = b.ravel()
print(b)

a_bool = (b > P)
a_bool = (data1*a_bool)
print('which we need to replace ', a_bool)

indexes = np.where(a_bool == 0)
print('indexes = ', indexes[0])

data1[indexes[0]]=data2[indexes[0]]
print('result = ', data1)