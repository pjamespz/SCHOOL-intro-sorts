#create a swapmap of 2logn pairs for any given n.
import random
import math

def genSwapmap(n):
    numpairs = math.trunc(2*math.log(n))
    i = []
    j = []
    for iter in range(1,numpairs+1):
        idx1 = random.randint(0,n-1)
        idx2 = random.randint(0,n-1)
        if idx1 not in i and idx1 not in j and idx2 not in i and idx2 not in j:
            i.append(idx1)
            j.append(idx2)
    return i, j

n = 100
data = []
for i in range(n):
    data.append(random.randint(0,1000))
idx1 = []
idx2 = []
idx1, idx2 = genSwapmap(n)
print(data)
for i, j in zip(idx1, idx2):
    data[i], data[j] = data[j], data[i]
print(data)