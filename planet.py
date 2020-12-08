import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

n = int(input("Enter the number of steps\n"))
s = int(n/2)


def f(r, u, t):
    return 1/r**3-1/r**2  # Equation of r


def g(theta, r, t):
    return 1/r**2  # Equation of theta


x_graph = []
y_graph = []


def func(r_0, theta_0, u_0, t_0, h):
    x = -0.98  
    y = 0      
    for i in range(1, n + 1):
        m1 = h * u_0
        k1 = h * f(r_0, u_0, t_0)
        l1 = h * g(theta_0, r_0, t_0)
        m2 = h * (u_0 + 0.5 * k1)
        k2 = h * f(r_0 + 0.5 * m1, u_0 + 0.5 * k1, t_0 + 0.5 * h)
        l2 = h * g(theta_0 + 0.5 * l1, r_0 + 0.5 * k1, t_0 + 0.5 * h)
        m3 = h * (u_0 + 0.5 * k2)
        k3 = h * f(r_0 + 0.5 * m2, u_0 + 0.5 * k2, t_0 + 0.5 * h)
        l3 = h * g(theta_0 + 0.5 * l2, r_0 + 0.5 * k2, t_0 + 0.5 * h)
        m4 = h * (u_0 + k3)
        k4 = h * f(r_0 + m3, u_0 + k3, t_0 + h)
        l4 = h * g(theta_0 + l3, r_0 + k3, t_0 + h)
        r_0 += (m1 + 2 * m2 + 2 * m3 + m4) / 6
        u_0 += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        theta_0 += (l1 + 2 * l2 + 2 * l3 + l4) / 6
        x = r_0 * np.cos(theta_0)
        y = r_0 * np.sin(theta_0)
        t_0 += h
        x_graph.append(x)
        y_graph.append(y)
    return x, y


def di():
    dist = 0
    for i in range(n-2):
        d = np.sqrt((x_graph[i+1] - x_graph[i]) ** 2 + (y_graph[i+1] - y_graph[i]) ** 2)
        dist += d
    return print(f'distance travelled = {dist}, coordinates = {(x_graph[n-1], y_graph[n-1])}')

# print(di())
print(func(0.98, -np.pi, 0, 0, 0.001))

fig, ax = plt.subplots()

ax.set(xlim = (-1.2,1.5), ylim = (-1.8,1.8), title = 'Planet\'s orbit')
# ax.get_xaxis().set_ticks([])
# ax.get_yaxis().set_ticks([])

trail = 200
def polar_animator(i, trail=200):
    l1.set_data(x_graph[i-trail:i], y_graph[i-trail:i])
    return l1,

l1, = ax.plot([],[], 'o-', color='#d2eeff',markevery=[-1], markerfacecolor='#0077BE')
l2, = ax.plot([-0.02],[0],marker= 'o',markerfacecolor='#FDB813', markersize=9, markeredgecolor='#FD7813')

ax.plot(-0.5,-1.6, 'o', color='#d2eeff', markerfacecolor='#0077BE')
ax.text(-0.46, -1.65, 'Planet')

ax.plot(0.36, -1.6, marker= 'o',markerfacecolor='#FDB813', markersize=9, markeredgecolor='#FD7813')
ax.text(0.4, -1.65, 'Sun')
ani = animation.FuncAnimation(fig, polar_animator, frames= len(x_graph), fargs=(trail,), interval=5, blit=True)
ani.save('planet.mp4', writer= 'ffmpeg')
# plt.show()
