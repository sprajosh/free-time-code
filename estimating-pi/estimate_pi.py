import matplotlib.pyplot as plt
import numpy.random as npr
import time

start = time.time()
c = 1000000
x = npr.uniform(size=c)
y = npr.uniform(size=c)

inside = x**2 + y**2 <= 1
outside = x**2 + y**2 > 1

inside_x = x[inside]
inside_y = y[inside]

outside_x = x[outside]
outside_y = y[outside]

print('Done in', time.time() - start, 'seconds')

plt.gca().set_aspect('equal', adjustable='box')
plt.scatter(outside_x, outside_y, marker='.', color='blue')
plt.scatter(inside_x, inside_y, marker='.', color='red')

print (4*len(x[inside])/c)
plt.show()