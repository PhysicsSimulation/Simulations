import numpy as np
from numpy import cos, sin, arange, pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation

h = 0.005   #the change in runge kutta
N = 5000 # iterations
L1=1    #length 1
L2=1.5  #lenth 2
m1=50  #mass of bob 1
m2=1    #mass of bob2
g = 9.81#gravity
theta_01 = (np.pi/180)*90
theta_02 = (np.pi/180)*60
w_1 = 0
w_2 = 0

# dw/dt function oft theta 1

def funcdwdt1(theta1,theta2,w1,w2):
    cos12 = cos(theta1 - theta2)#for wrirting the main equation in less complex manner
    sin12 = sin(theta1 - theta2)
    sin1 = sin(theta1)
    sin2 = sin(theta2)
    denom = cos12**2*m2 - m1 - m2
    ans = ( L1*m2*cos12*sin12*w1**2 + L2*m2*sin12*w2**2
            - m2*g*cos12*sin2      + (m1 + m2)*g*sin1)/(L1*denom)
    return ans

# dw/dt function oft thetas 2
    
def funcdwdt2(theta2,theta1,w1,w2):
    cos12 = cos(theta1 - theta2)
    sin12 = sin(theta1 - theta2)
    sin1 = sin(theta1)
    sin2 = sin(theta2)
    denom = cos12**2*m2 - m1 - m2
    ans2 = -( L2*m2*cos12*sin12*w2**2 + L1*(m1 + m2)*sin12*w1**2
            + (m1 + m2)*g*sin1*cos12  - (m1 + m2)*g*sin2 )/(L2*denom)
    return  ans2

# d0/dt function for theta 1

def funcd0dt1(w0):
    return w0

# d0/dt function for theta 2
    
def funcd0dt2(w0):
    return w0


X1= []
X2= []
Y1= []
Y2= []

def func(w1,w2, theta1,theta2): 
	for i in range(N):
	    k1a = h * funcd0dt1(w1)  # gives theta1
	    k1b = h * funcdwdt1(theta1,theta2,w1,w2)  # gives omega1
	    k1c = h * funcd0dt2(w2)  # gives theta2
	    k1d = h * funcdwdt2(theta2,theta1,w1,w2)   # gives omega2

	    k2a = h * funcd0dt1(w1 + (0.5 * k1b))
	    k2b = h * funcdwdt1(theta1 + (0.5 * k1a),theta2,w1,w2)
	    k2c = h * funcd0dt2(w2 + (0.5 * k1d))
	    k2d = h * funcdwdt2(theta2 + (0.5 * k1c),theta1,w1,w2)

	    k3a = h * funcd0dt1(w1 + (0.5 * k2b))
	    k3b = h * funcdwdt1(theta1 + (0.5 * k2a),theta2,w1,w2)
	    k3c = h * funcd0dt2(w2 + (0.5 * k2d))
	    k3d = h * funcdwdt2(theta2 + (0.5 * k2c),theta1,w1,w2)

	    k4a = h * funcd0dt1(w1 + k3b)
	    k4b = h * funcdwdt1(theta1 + k3a,theta2,w1,w2)
	    k4c = h * funcd0dt2(w2 + k3d)
	    k4d = h * funcdwdt2(theta2 + k3c,theta1,w1,w2)

	    #addidng the vakue aftyer the iterartions
	    theta1 += 1 / 6 * (k1a + 2 * k2a + 2 * k3a + k4a)  
	    w1 +=1 / 6 * (k1b + 2 * k2b + 2 * k3b + k4b)             
	    theta2 += + 1 / 6 * (k1c + 2 * k2c + 2 * k3c + k4c)     
	    w2 += 1 / 6 * (k1d + 2 * k2d + 2 * k3d + k4d)
	    x1 = L1 * sin(theta1)
	    y1 = -L1 * cos(theta1)
	    x2 = x1 + L2 * sin(theta2)
	    y2 = y1 - L2 * cos(theta2)
	    X1.append(x1)
	    X2.append(x2)
	    Y1.append(y1)
	    Y2.append(y2)    
	return x1,y1,x2,y2


print(func(w_1, w_2, theta_01, theta_02))

fig, ax = plt.subplots()
l1, = ax.plot([], [],'o-', markevery=[-1])
l2, = ax.plot([],[],'o-', markevery=[-1])
l3, = ax.plot([],[], '-o',color='#805DA5', lw=2, ms=8)

ax.set(xlim=(-3, 3), ylim=(-3,3))
# ax.grid()
trail = len(X1)

def animate(i, trail=len(X1)):
    l1.set_data(X1[:i], Y1[:i])
    l2.set_data(X2[:i], Y2[:i])
    l3.set_data([0,X1[i], X2[i]], [0,Y1[i],Y2[i]])
    return l1, l2, l3,

ani = animation.FuncAnimation(fig, animate, interval = 10, fargs= (trail,),frames=len(X1))
ani.save('save.mp4', writer='ffmpeg')
