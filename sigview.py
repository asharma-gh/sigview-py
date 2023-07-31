import sys
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
pi=np.pi
matplotlib.use('TKAgg')

def on_press(e):
    sys.stdout.flush()
    if e.key == 'q':
        sys.exit(0)

def _phase_ang(x, t, xi=1, ts=1):
    return (2*pi*x*xi) - (2*pi*t/ts)

# animate :D
fig, ax = plt.subplots()
fig.canvas.mpl_connect('key_press_event', on_press)
def animate(ii):
    ii = ii % 100
    ax.clear()
    x = np.arange(100)
    y = np.cos(_phase_ang(x, ii, xi=1/100, ts=50))
    ax.plot(x,y)

an = animation.FuncAnimation(fig, animate, interval=10)
plt.show()

