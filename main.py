import math
import numpy
from matplotlib import pyplot

n = 500

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

