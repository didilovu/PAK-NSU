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

data0 = zip(data1, data2)
data0 = list(data0)
print(data0)

ch = [0,1]

arr1 = np.random.choice(ch, len(data1), p=[1-P, P])
print(arr1)

data1[arr1>0] = data2[arr1>0]

print(data1)