# simple reference for pyplot

import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2

import matplotlib.pyplot as plt
%matplotlib inline # For notebook
# plt.show() - for .py file

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,1.1,1.1])
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')


###########################################################################
# Two axes - color, limits
##########################################################################

fig = plt.figure()

ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,.2,.2])

ax1.plot(x,z, color='red')
ax1.set_title('full')
ax1.set_xlabel('X')
ax1.set_ylabel('Z')

ax2.plot(x,y)
ax2.set_title('zoom')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_xlim([20,22])
ax2.set_ylim([30,50])

##########################################################################
## Sub Plots - line width, linestyle
##########################################################################

fig, axes = plt.subplots(1, 2, figsize=(12,4)) #1 column by 2 rows
axes[0].plot(x, y, ls='--', lw=3) # line-style and line-width
axes[1].plot(x, z, color = 'red', lw=3)
