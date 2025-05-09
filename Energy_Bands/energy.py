import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt



data = genfromtxt('siesta.bands', delimiter="\t", filling_values="NaN")


print(data)

"""
np.loadtxt('siesta.bands')

k = data [:, 0]
data = []
with open('siesta.bands') as f:
    for line in f:
        if line.strip() == "" or not line.strip()[0].replace('.','',1). replace('.','',1).isdigit():
            continue
        data.append([float(x) for x in line.split()])

data = np
for i in range(1, data.shape[1]):
    plt.plot(k, data[:, i])
plt.xlabel(K)
plt.ylabel(E (ev))
plt.show() 
"""