"""
This code creates a 3d graph that plots random points.
I found these libraries on the internet but for it to work 
properly I had to install 'pip3 install numpy matplotlib'
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z)

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

plt.show()
