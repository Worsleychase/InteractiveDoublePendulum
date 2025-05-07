import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.animation import FuncAnimation

# Initial parameters (can be modified with sliders)
L1 = 1.0
L2 = 1.0
m1 = 1.0
m2 = 1.0
g = 9.81

# Initial conditions: [theta1, omega1, theta2, omega2]
state = np.array([np.pi / 2, 0, np.pi / 2, 0], dtype=float)

dt = 0.02 # Change for simulation speed

def derivs(state, L1, L2, m1, m2):
    theta1, omega1, theta2, omega2 = state
    delta = theta2 - theta1

    denom1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta)**2
    denom2 = (L2 / L1) * denom1

    domega1 = (m2 * L1 * omega1**2 * np.sin(delta) * np.cos(delta) +
           m2 * g * np.sin(theta2) * np.cos(delta) +
           m2 * L2 * omega2**2 * np.sin(delta) -
           (m1 + m2) * g * np.sin(theta1)) / denom1

    domega2 = (-m2 * L2 * omega2**2 * np.sin(delta) * np.cos(delta) +
           (m1 + m2) * g * np.sin(theta1) * np.cos(delta) -
           (m1 + m2) * L1 * omega1**2 * np.sin(delta) -
           (m1 + m2) * g * np.sin(theta2)) / denom2

    return np.array([omega1, domega1, omega2, domega2])

def step():
    global state
    k1 = derivs(state, L1, L2, m1, m2)
    k2 = derivs(state + 0.5 * dt * k1, L1, L2, m1, m2)
    k3 = derivs(state + 0.5 * dt * k2, L1, L2, m1, m2)
    k4 = derivs(state + dt * k3, L1, L2, m1, m2)
    state += (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

def getPos():
    theta1, _, theta2, _ = state
    x1 = L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)
    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 - L2 * np.cos(theta2)
    return x1, y1, x2, y2

# Plot setup
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.35)
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
line, = ax.plot([], [], 'o-', lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    step()
    x1, y1, x2, y2 = getPos()
    line.set_data([0, x1, x2], [0, y1, y2])
    return line,

ani = FuncAnimation(fig, update, init_func=init, blit=True, interval=20)

# Sliders
axcolor = 'lightgoldenrodyellow'
ax_m1 = plt.axes([0.1, 0.25, 0.8, 0.03], facecolor=axcolor)
ax_m2 = plt.axes([0.1, 0.2, 0.8, 0.03], facecolor=axcolor)
ax_L1 = plt.axes([0.1, 0.15, 0.8, 0.03], facecolor=axcolor)
ax_L2 = plt.axes([0.1, 0.1, 0.8, 0.03], facecolor=axcolor)
ax_g  = plt.axes([0.1, 0.05, 0.8, 0.03], facecolor=axcolor)

slider_m1 = Slider(ax_m1, 'Mass 1', 0.1, 5.0, valinit=m1)
slider_m2 = Slider(ax_m2, 'Mass 2', 0.1, 5.0, valinit=m2)
slider_L1 = Slider(ax_L1, 'Length 1', 0.1, 2.0, valinit=L1)
slider_L2 = Slider(ax_L2, 'Length 2', 0.1, 2.0, valinit=L2)
slider_g  = Slider(ax_g, 'Gravity', 0.1, 2.0, valinit=g)

def update_sliders(val):
    global m1, m2, L1, L2, g
    m1 = slider_m1.val
    m2 = slider_m2.val
    L1 = slider_L1.val
    L2 = slider_L2.val
    g = slider_g.val

slider_m1.on_changed(update_sliders)
slider_m2.on_changed(update_sliders)
slider_L1.on_changed(update_sliders)
slider_L2.on_changed(update_sliders)
slider_g.on_changed(update_sliders)

plt.show()
