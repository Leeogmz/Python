import numpy as np


print(np.loadtxt('apples_ts.csv', delimiter=',', usecols=np.arange(1,88, 1)))