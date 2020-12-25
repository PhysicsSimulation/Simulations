import matplotlib.pyplot as plt
import matplotlib.animation as animation
n = int(input("Enter the number\n"))
N_t = []
alpha = 1.5251
beta = 1.5181
gamma = 0.5
delta = 0.13
lamb = 3.72*10**(-4)
mu = 1.76*10**(-4)
for i in range(n):
	N_t.append(1+(lamb-mu)*i/100)
def ds(s, i, e, N, t):
    return - alpha*s*i - alpha*s*e + lamb*N - mu*s


def de(e, s, i, t):
    return alpha*s*i +  alpha*s*e - beta*e - mu*e


def di(i, e):
    return beta*e - (gamma+delta)*i - mu*i


def dr(r, i, t):
    return gamma*i - mu*r


def dd(d, i, t):
    return delta*i


s_graph = []
i_graph = []
r_graph = []
d_graph = []
t_graph = []
e_graph = []
def func(s0, e0, i0, r0, d0, t0, h):
    ds_dt = 0
    de_dt = 0
    di_dt = 0
    dr_dt = 0
    dd_dt = 0
    cumulative = 0
    for i in range(n):
        ds1 = h*ds(s0, i0, e0, N_t[i],t0)
        de1 = h*de(e0, s0, i0, t0)
        di1 = h*di(i0, e0)
        dr1 = h*dr(r0, i0, t0)
        dd1 = h*dd(d0, i0, t0)
        ds2 = h*ds(s0 + 0.5*ds1, i0 + 0.5*di1, e0 + 0.5*de1, N_t[i],t0 + 0.5*h)
        de2 = h*de(e0 + 0.5*de1, s0 + 0.5*ds1, i0 + 0.5*di1, t0 + 0.5*h)
        di2 = h*di(i0 + 0.5 * di1, e0 + 0.5 * de1)
        dr2 = h*dr(r0 + 0.5*dr1, i0 + 0.5*di1, t0 + 0.5*h)
        dd2 = h*dd(d0 + 0.5*dd1, i0 + 0.5*di1, t0 + 0.5*h)
        ds3 = h*ds(s0 + 0.5*ds2, i0 + 0.5*di2, e0 + 0.5*de2, N_t[i], t0 + 0.5*h)
        de3 = h*de(e0 + 0.5*de2, s0 + 0.5*ds2, i0 + 0.5*di2, t0 + 0.5*h)
        di3 = h*di(i0 + 0.5 * di2, e0 + 0.5 * de2)
        dr3 = h*dr(r0 + 0.5*dr2, i0 + 0.5*di2, t0 + 0.5*h)
        dd3 = h*dd(d0 + 0.5*dd2, i0 + 0.5*di2, t0 + 0.5*h)
        ds4 = h*ds(s0 + ds3, i0 + di3, e0 + de3, N_t[i], t0 + h)
        de4 = h*de(e0 + de3, s0 + ds3, i0 + di3, t0 + h)
        di4 = h*di(i0 + di3, e0 + de3)
        dr4 = h*dr(r0 + dr3, i0 + di3, t0 + h)
        dd4 = h*dd(d0 + dd3, i0 + di3, t0 + h)
        s0 += (ds1 + 2*ds2 + 2*ds3 + ds4)/6
        e0 += (de1 + 2*de2 + 2*de3 + de4)/6
        i0 += (di1 + 2*di2 + 2*di3 + di4)/6
        r0 += (dr1 + 2*dr2 + 2*dr3 + dr4)/6
        d0 += (dd1 + 2*dd2 + 2*dd3 + dd4)/6
        t0 += h
        i_graph.append(i0)
        r_graph.append(r0)
        d_graph.append(d0)
        t_graph.append(t0)
        s_graph.append(s0)
        e_graph.append(e0)
        cumulative += h*(1.8181*e_graph[i])
    return s0, e0, i0, r0, d0, cumulative

print(func(1, 0, 0.001, 0, 0, 0, 0.001))

fig, ax = plt.subplots()

ax.set(xlim=(0, len(t_graph)/1000), ylim=(-0.05,1), title='Pandemic Simulation')
# ax.grid()
trail = 100

def animate(i, trail=100):
    l1.set_data(t_graph[:i],i_graph[:i])
    l2.set_data(t_graph[:i],r_graph[:i])
    l3.set_data(t_graph[:i],d_graph[:i])

    return l1, l2,l3,

l1, = ax.plot([],[], 'o-',markevery=[-1], label='Infected')
l2, = ax.plot([],[], 'o-',markevery=[-1], label='Recovered')
l3, = ax.plot([],[], 'o-',markevery=[-1], label='Deceased')

ani = animation.FuncAnimation(fig, animate,frames=len(t_graph),fargs=(trail,),interval =5, blit=True)
# plt.plot(t_graph, i_graph)
# plt.plot(t_graph, r_graph)
# plt.plot(t_graph, d_graph)
# plt.show()
plt.legend()
ani.save('pandemic.mp4', writer='ffmpeg')