import matplotlib.pyplot as plt 
from pylab import randn
x= randn(100)
y= randn(100)
plt.scatter(x,y,color="r")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()

#