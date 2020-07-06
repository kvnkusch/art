import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

y_star = 1
c = 0.2
k = 0.8
a_1 = -0.6
a_2 = -0.5
p = 1.8

x_0 = 1
y_0 = 1
z_0 = 1

xs = [x_0]
ys = [y_0]
zs = [z_0]

initial_iterations = 10000
iterations_step =    100
total_iterations =   100000

for t in range(total_iterations):
  x_t = ys[t]
  y_t = k * (y_star - zs[t] * ys[t]) - a_1 * ys[t] - a_2 * xs[t]
  z_t_numerator = p * ys[t] * (k * (y_star - zs[t] * ys[t]) - y_star - a_1 * ys[t] - a_2 * xs[t])
  z_t_denominator = c + ys[t] ** 2
  z_t = zs[t] + z_t_numerator / z_t_denominator

  xs.append(x_t)
  ys.append(y_t)
  zs.append(z_t)

for t in range (initial_iterations, total_iterations, iterations_step):
  graph_xs = xs[t:t + iterations_step]
  graph_ys = ys[t:t + iterations_step]
  graph_zs = zs[t:t + iterations_step]
  plt.plot(graph_ys, graph_zs, 'o', markersize=1, c=numpy.random.rand(3,))

# graph_xs = xs[initial_iterations:]
# graph_ys = ys[initial_iterations:]
# graph_zs = zs[initial_iterations:]

# plt.plot(graph_ys, graph_zs, 'o', markersize=1)
plt.show()

# fig = plt.figure()
# ax = Axes3D(fig)

# ax.scatter(graph_xs, graph_ys, graph_zs, marker='.')
# plt.show()
