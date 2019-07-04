import math
import numpy
from matplotlib import pyplot

n = 50

x_start, x_end = -5.0,5.0
y_start, y_end = -10.0,10.0
x = numpy.linspace(x_start,x_end,n)
y = numpy.linspace(y_start,y_end,n)
X,Y = numpy.meshgrid(x,y) # simulated particles not in motion
## visualize

width = 10.0
height = (y_end-y_start)/(x_end-x_start) * width
pyplot.figure(figsize=(width,height))

pyplot.xlim(x_start,x_end)
pyplot.ylim(y_start,y_end)
pyplot.scatter(X,Y,s=5,color='#CD2305',marker='o')
pyplot.show()

## source

strength = 5.0
x_source, y_source = -1.0,0 ## location

u_source = (strength / (2 * math.pi) * (X - x_source) / ((X - x_source)**2 + (Y - y_source)**2))
v_source = (strength / (2 * math.pi) *(Y - y_source) / ((X - x_source)**2 + (Y - y_source)**2))

## streams

width = 10.0
height = (y_end-y_start)/(x_end-x_start) * width
pyplot.figure(figsize=(width,height))
pyplot.xlim(x_start,x_end)
pyplot.ylim(y_start,y_end)
pyplot.streamplot(X,Y, u_source, v_source, density=2, linewidth=1, arrowsize=2, arrowstyle='->')

pyplot.scatter(x_source,y_source,s=80,color='#CD2305',marker='o')
pyplot.show() 
