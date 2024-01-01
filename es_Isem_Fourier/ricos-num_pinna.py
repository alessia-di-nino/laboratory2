# 8 grafici simulazione integratore frequenze spaziate logaritmicamente tra le due frequenze di taglio
#cut-off frequency = 1/2piRC
#valutare l'accordo della ricostruzione con i dati presi

import numpy as np
import pylab
import math
from math import exp
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

f = np.logspace(math.log10(0.05), math.log10(1100), 8)
n = 1000
x1 = np.linspace(-2/f[1], 2/f[1], 5000)
f1 = np.full(len(x1), f[1])
y1 = sum((2/(i*np.pi))*(1/np.sqrt(1+((i*2*np.pi*f1)/(1/(33000*4.7*10**(-6))))**2))*np.sin(i*2*np.pi*f1*x1 + np.arctan(-(i*2*np.pi*f1)/(1/(33000*4.7*10**(-6))))) for i in range(1, n, 2))


x2 = np.linspace(-2/f[2], 2/f[2], 5000)
f2 = np.full(len(x2), f[2])
y2 = sum((2/(i*np.pi))*(1/np.sqrt(1+((i*2*np.pi*f2)/(1/(33000*4.7*10**(-6))))**2))*np.sin(i*2*np.pi*f2*x2 + np.arctan(-(i*2*np.pi*f2)/(1/(33000*4.7*10**(-6))))) for i in range(1, n, 2))


x3 = np.linspace(-2/f[3], 2/f[3], 5000)
f3 = np.full(len(x3), f[3])
y3 = sum((2/(i*np.pi))*(1/np.sqrt(1+((i*2*np.pi*f3)/(1/(33000*4.7*10**(-6))))**2))*np.sin(i*2*np.pi*f3*x3 + np.arctan(-(i*2*np.pi*f3)/(1/(33000*4.7*10**(-6))))) for i in range(1, n, 2))


x4 = np.linspace(-2/f[4], 2/f[4], 5000)
f4 = np.full(len(x4), f[4])
y4 = sum((2/(i*np.pi))*(1/np.sqrt(1+((i*2*np.pi*f4)/(1/(33000*4.7*10**(-6))))**2))*np.sin(i*2*np.pi*f4*x4 + np.arctan(-(i*2*np.pi*f4)/(1/(33000*4.7*10**(-6))))) for i in range(1, n, 2))


x5 = np.linspace(-2/f[5], 2/f[5], 5000)
f5 = np.full(len(x4), f[5])
y5 = sum((2/(i*np.pi))*(1/np.sqrt(1+((i*2*np.pi*f5)/(1/(33000*4.7*10**(-6))))**2))*np.sin(i*2*np.pi*f5*x5 + np.arctan(-(i*2*np.pi*f5)/(1/(33000*4.7*10**(-6))))) for i in range(1, n, 2))


x6 = np.linspace(-2/f[6], 2/f[6], 5000)
f6 = np.full(len(x6), f[6])
y6 = sum((2/(i*np.pi))*(1/np.sqrt(1+((i*2*np.pi*f6)/(1/(33000*4.7*10**(-6))))**2))*np.sin(i*2*np.pi*f6*x6 + np.arctan(-(i*2*np.pi*f6)/(1/(33000*4.7*10**(-6))))) for i in range(1, n, 2))


x7 = np.linspace(-2/f[7], 2/f[7], 5000)
f7 = np.full(len(x7), f[7])
y7 = sum((2/(i*np.pi))*(1/np.sqrt(1+((i*2*np.pi*f7)/(1/(33000*4.7*10**(-6))))**2))*np.sin(i*2*np.pi*f7*x7 + np.arctan(-(i*2*np.pi*f7)/(1/(33000*4.7*10**(-6))))) for i in range(1, n, 2))


x0 = np.linspace(-2/f[0], 2/f[0], 5000)
f0 = np.full(len(x0), f[0])
y0 = sum((2/(i*np.pi))*(1/np.sqrt(1+((i*2*np.pi*f0)/(1/(33000*4.7*10**(-6))))**2))*np.sin(i*2*np.pi*f0*x0 + np.arctan(-(i*2*np.pi*f0)/(1/(33000*4.7*10**(-6))))) for i in range(1, n, 2))

plt.subplot(4, 2, 1)
plt.plot(x0, y0, color="lightblue")
plt.annotate("$f=0.05$ Hz", xy=(0.9, 0.3), xycoords='axes fraction',
            size=8, ha='right', va='top',
            bbox=dict(boxstyle='round', fc='w'))


plt.subplot(4, 2, 2)
plt.plot(x1, y1, color="lightblue")
plt.annotate("$f=0.2$ Hz", xy=(0.9, 0.3), xycoords='axes fraction',
            size=8, ha='right', va='top',
            bbox=dict(boxstyle='round', fc='w'))

plt.subplot(4, 2, 3)
plt.plot(x2, y2, color="lightblue")
plt.annotate("$f=0.8$ Hz", xy=(0.9, 0.3), xycoords='axes fraction',
            size=8, ha='right', va='top',
            bbox=dict(boxstyle='round', fc='w'))
plt.ylabel("[un. arb.]")

plt.subplot(4, 2, 4)
plt.plot(x3, y3, color="lightblue")
plt.annotate("$f=3.6$ Hz", xy=(0.9, 0.3), xycoords='axes fraction',
            size=8, ha='right', va='top',
            bbox=dict(boxstyle='round', fc='w'))


plt.subplot(4, 2, 5)
plt.plot(x4, y4, color="lightblue", label="frequenza")
plt.annotate("$f=15.1$ Hz", xy=(0.9, 0.3), xycoords='axes fraction',
            size=8, ha='right', va='top',
            bbox=dict(boxstyle='round', fc='w'))


plt.subplot(4, 2, 6)
plt.plot(x5, y5, color="lightblue")
plt.annotate("$f=63.2$ Hz", xy=(0.9, 0.3), xycoords='axes fraction',
            size=8, ha='right', va='top',
            bbox=dict(boxstyle='round', fc='w'))



plt.subplot(4, 2, 7)
plt.plot(x6, y6, color="lightblue")
plt.annotate("$f=263$ Hz", xy=(0.9, 0.3), xycoords='axes fraction',
            size=8, ha='right', va='top',
            bbox=dict(boxstyle='round', fc='w'))
plt.xlabel('Time [s]')

plt.subplot(4, 2, 8)
plt.plot(x7, y7, color="lightblue")
plt.annotate("$f=1100$ Hz", xy=(0.9, 0.3), xycoords='axes fraction',
            size=8, ha='right', va='top',
            bbox=dict(boxstyle='round', fc='w'))
plt.xlabel('Time [s]')



print(f)
plt.show()