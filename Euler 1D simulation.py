#!/usr/bin/env python
# coding: utf-8

# # 1D calculation of trajectory
# Calculate the trajectory and velocity as a function of time and distance if the force as a function of distance is given.

# In[50]:


import numpy as np
import matplotlib.pyplot as plt

# defining the boundary condition/initial conditions
v_int=0  #initial Velocity
x_int=-5  #initial distance
t_int=0 #final time
mass=1 #mass

#step wise increase in time 
#time= np.linspace(0,1,100) # np.linspace(start,stop, number of points betweent them)
#time2= np.arange(0,1,0.01)    #np.arange(start,stop-1,step)

x_t= [x_int] #empty list for postions
v_t= [v_int] #empty list for velocity
t_t= [t_int]

#defined force
def f(x):
        return np.sin(5*x) #defining 1D force


v= v_int
x= x_int
t= t_int
dt=0.01
for i in range(0,1001):
    t= t+dt
    x= x + v*dt
    v= v + f(x)*dt
    """
    x_t= np.append(x_t,x) #this way is correct but it makes the calculations lengthy 
    v_t= np.append(v_t,v) # because np.append() creates a new array every time → inefficient →very slow for large loops..
    t_t= np.append(t_t,t) # instead create an array once as shown in the next line
    """
    x_t.append(x)
    v_t.append(v)
    t_t.append(t)
    
x_t= np.array(x_t)  ## Convert to numpy arrays (if needed for plotting or math ops)
v_t= np.array(v_t)
t_t= np.array(t_t)

plt.plot(t_t,x_t)
plt.xlabel("time")
plt.ylabel("distance")
plt.title("Distance vs time")
plt.show()

plt.plot(t_t,v_t)
plt.xlabel("time")
plt.ylabel("velocity")
plt.title("velocity vs time")
plt.show()

plt.plot(x_t,v_t)
plt.xlabel("distance")
plt.ylabel("velocity")
plt.title("Distance vs velocity")
plt.show()
