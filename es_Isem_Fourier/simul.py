#simulazione pinna di squalo con frquenze 13, 80, 176, 333. 1000 iterazioni, 5000 punti, scritti direttamente con w e non con f, R=3300 e C=10-6.

import matplotlib.pyplot as plt
import numpy as np

n = 1000
x1 = np.linspace(0, .3,5000)
f1 = np.full(len(x1), 13)
y1 = sum((2/(i*np.pi))*(1/np.sqrt(1+((i*2*np.pi*f1)/(1/(3300*10**(-6))))**2))*np.sin(i*2*np.pi*f1*x1 + np.arctan(-(i*2*np.pi*f1)/(1/(3300*10**(-6))))) for i in range(1, n, 2))


x2 = np.linspace(0, .05,5000)
f2 = np.full(len(x2), 80)
y2 = sum((2/(i*np.pi))*(1/np.sqrt(1+((i*2*np.pi*f2)/(1/(3300*10**(-6))))**2))*np.sin(i*2*np.pi*f2*x2 + np.arctan(-(i*2*np.pi*f2)/(1/(3300*10**(-6))))) for i in range(1, n, 2))


x3 = np.linspace(0, .023,5000)
f3 = np.full(len(x3), 176)
y3 = sum((2/(i*np.pi))*(1/np.sqrt(1+((i*2*np.pi*f3)/(1/(3300*10**(-6))))**2))*np.sin(i*2*np.pi*f3*x3 + np.arctan(-(i*2*np.pi*f3)/(1/(3300*10**(-6))))) for i in range(1, n, 2))


x4 = np.linspace(0, .012,5000)
f4 = np.full(len(x4), 333)
y4 = sum((2/(i*np.pi))*(1/np.sqrt(1+((i*2*np.pi*f4)/(1/(3300*10**(-6))))**2))*np.sin(i*2*np.pi*f4*x4 + np.arctan(-(i*2*np.pi*f4)/(1/(3300*10**(-6))))) for i in range(1, n, 2))


plt.subplot(2, 2, 1)
plt.plot(x1, y1, color="lightblue")
#plt.legend(loc="upper left", frameon=False)
plt.annotate("$f=(13.01)$ Hz", xy=(110, 110), xycoords='axes points',
            size=8, ha='right', va='top',
            bbox=dict(boxstyle='round', fc='w'))
plt.ylim(-0.6,0.6)


plt.subplot(2, 2, 2)
plt.plot(x2, y2, color="lightblue")
#plt.legend(loc="upper left", frameon=False)
plt.annotate("$f=(80.2)$ Hz", xy=(110, 110), xycoords='axes points',
            size=8, ha='right', va='top',
            bbox=dict(boxstyle='round', fc='w'))
plt.ylim(-0.5,0.5)


plt.subplot(2, 2, 3)
plt.plot(x3, y3, color="lightblue")
#plt.legend(loc="upper left", frameon=False)
plt.annotate("$f=(176.1)$ Hz", xy=(110, 110), xycoords='axes points',
            size=8, ha='right', va='top',
            bbox=dict(boxstyle='round', fc='w'))
plt.ylim(-0.5,0.5)
plt.xlabel('Time [s]')
plt.ylabel("                                             [un. arb.]")

plt.subplot(2, 2, 4)
plt.plot(x4, y4, color="lightblue")
#plt.legend(loc="upper left", frameon=False)
plt.annotate("$f=(333.2)$ Hz", xy=(110, 110), xycoords='axes points',
            size=8, ha='right', va='top',
            bbox=dict(boxstyle='round', fc='w'))
plt.ylim(-0.5,0.5)
plt.xlabel('Time [s]')


plt.show()