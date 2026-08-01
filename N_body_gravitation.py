import numpy as np
import matplotlib.pyplot as plt
import time
import winsound as ws
from matplotlib.animation import FuncAnimation

### units will be expressed as year, solar mass and AU

G= 4* (np.pi)**2 

### the sun and the 8 planets

# initial coordinates 
def position():
    # Initial x coordinates
    x = [
    0,       # Sun
    0.47,    # Mercury
    0.72,    # Venus
    1,       # Earth
    1.5237,  # Mars
    5.2,     # Jupiter
    9.36,    # Saturn
    19.18,   # Uranus
    30.1     # Neptune
]
    # Initial y coordinates
    y = [
    0,  # Sun
    0,  # mercury
    0,  # Venus
    0,  # earth
    0,  # Mars
    0,  # Jupiter
    0,  # Saturn
    0,  # Uranus
    0   # Neptune
] 
    
    return x, y

x, y = position()

def velocities():
    # Initial velocity components (AU/year)
    vx = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Initial tangential velocities (AU/year)
    vy = [
    0,                  # Sun
    9.95,               # Mercury
    7.38,               # Venus
    6.281991687112502,  # Earth
    5.0867271316753815, # Mars
    2.74,               # Jupiter
    2.04,               # Saturn
    1.26,               # Uranus
    1.145               # Neptune

]
    return vx, vy

vx, vy = velocities()

def position_storages():
    # Lists storing the x coordinates during the simulation
    xpos = [[], [], [], [], [], [], [], [], []]

    # Lists storing the y coordinates during the simulation
    ypos = [[], [], [], [], [], [], [], [], []]

    return xpos, ypos

xpos, ypos = position_storages()


def masses():
    # Masses expressed in solar masses
    mass = [
    1,                          # Sun
    1.65e-07,                   # Mercury
    2.447e-06,                  # Venus
    3.002513826043238e-06,      # Earth
    3.2267471091000503e-07,     # Mars
    5.0278543100000007166e-04,  # Jupiter
    2.86e-04,                   # Saturn
    4.36e-05,                   # Uranus
    5.15e-05                    # Neptune
]
    return mass

mass = masses()

def acceleration():
    # Acceleration components
    ax = [0] * 10
    ay = [0] * 10

    return ax, ay

ax, ay = acceleration()



# Time step (years)
dt = 0.0001

begin= time.time()

def symplectic_euler_integrator(x, y, vx, vy, xpos, ypos, mass, ax, ay):
    # Symplectic Euler integration
    for i in range(10**5):
        # the i loop is the number of time we want 
        # our program to run
        for j in range(len(x)):
            for k in range(len(x)):
                # these two nested loops are for calculating
                # the interaction between the bodies
                if j != k:
                  ax[j] += -G * mass[k] * (x[j] - x[k]) / (((x[j]-x[k])**2 + (y[j]-y[k])**2)**0.5)**3
                  ay[j] += -G * mass[k] * (y[j] - y[k]) / (((x[j]-x[k])**2 + (y[j]-y[k])**2)**0.5)**3

        for l in range(len(x)):
            # Velocity update
            vx[l] += ax[l] * dt
            vy[l] += ay[l] * dt
            
            # Store trajectory
            xpos[l].append(x[l])
            ypos[l].append(y[l])
            
            # Position update
            x[l] += vx[l] * dt
            y[l] += vy[l] * dt

            # reset the accelerations to zeros    
        for m in range(len(ax)):
            ax[m]=0
            ay[m]=0

    return xpos, ypos

xposition, yposition = symplectic_euler_integrator(x, y, vx, vy, xpos, ypos, mass, ax, ay)

        
end_time = time.time()

# Audible notification when the simulation is finished
ws.Beep(400, 1000)

plt.plot(xpos[0], ypos[0], label="Sun",      color="gold")
plt.plot(xpos[1], ypos[1], label="Mercury",  color="dimgray")
plt.plot(xpos[2], ypos[2], label="Venus",    color="goldenrod")
plt.plot(xpos[3], ypos[3], label="Earth",    color="dodgerblue")
plt.plot(xpos[4], ypos[4], label="Mars",     color="firebrick")
plt.plot(xpos[5], ypos[5], label="Jupiter",  color="peru")
plt.plot(xpos[6], ypos[6], label="Saturn",   color="khaki")
plt.plot(xpos[7], ypos[7], label="Uranus",   color="turquoise")
plt.plot(xpos[8], ypos[8], label="Neptune",  color="royalblue")

plt.legend()
plt.show()


