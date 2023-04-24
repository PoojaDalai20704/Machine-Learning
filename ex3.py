#Numpy
import numpy as np
arr = np.array([1, 2, 3, 4, 5]) print(arr)
print(type(arr))

#Panda
import pandas as pd
df = pd.read_csv('data.csv') print(df.to_string())

#Mathplot Lib import sys
import matplotlib matplotlib.use('Agg')
import matplotlib.pyplot as plt import numpy as np
xpoints = np.array([0, 6]) ypoints = np.array([0, 250]) plt.plot(xpoints, ypoints) plt.show() plt.savefig(sys.stdout.buffer) sys.stdout.flush()
