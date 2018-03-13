import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import svm


x = np.array([[1,180.3],
             [1,135.5],
             [1,141.5],
             [2,128.8],
             [2,124.2],
             [2,94.67]])
y = [0,1,0,1,0,1]
plt.scatter(x,y)
plt.show()
