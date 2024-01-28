##Treno di impulsi: formula in Fourier
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
delta = np.full(1, 0.5)
n = 10000
x = np.linspace(-2/1000, 2/1000,2000)
y = delta + sum((2/(k*np.pi))*np.cos(k*2*np.pi*1000*x)*np.sin((k*np.pi*delta)) for k in range(1, n, 1))
y1 = delta + sum((2/(k*np.pi))*(1/np.sqrt(1+((k*1000)/10)**2))*np.cos(k*2*np.pi*1000*x)*np.sin((k*np.pi*delta)+np.arctan(-((k*1000)/10))) for k in range(1, n, 1))

plt.plot(x,y)
plt.plot(x,y1, color="red")
plt.show()

##Treno di impulsi dopo integratore
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
delta = np.full(1, 0.5)
n = 10000
x1 = np.linspace(-2/1000, 2/1000,2000)
y1 = delta + sum((2/(k*np.pi))*(1/np.sqrt(1+((k*1000)/10)**2))*np.cos(k*2*np.pi*1000*x)*np.sin((k*np.pi*delta)+np.arctan(-((k*1000)/10))) for k in range(1, n, 1))

plt.plot(x1,y1, color="red")
plt.show()

##6 grafici simulazione treno di impulsi duty cycle
import numpy as np
import pylab
import math
from math import exp
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

delta = np.linspace(0.1, 0.9, 6)
n = 100000

delta0 = np.full(1, delta[0])
x00 = np.linspace(-2/1000, 2/1000,5000)
y0 = delta0 + sum((2/(k*np.pi))*np.cos(k*2*np.pi*1000*x00)*np.sin((k*np.pi*delta0)) for k in range(1, n, 1))
y00 = delta0 + sum((2/(k*np.pi))*(1/np.sqrt(1+((k*1000)/10)**2))*np.cos(k*2*np.pi*1000*x00)*np.sin((k*np.pi*delta0)+np.arctan(-((k*1000)/10))) for k in range(1, n, 1))


delta1 = np.full(1, delta[1])
x11 = np.linspace(-2/1000, 2/1000,2000)
y1 = delta1 + sum((2/(k*np.pi))*np.cos(k*2*np.pi*1000*x11)*np.sin((k*np.pi*delta1)) for k in range(1, n, 1))
y11 = delta1 + sum((2/(k*np.pi))*(1/np.sqrt(1+((k*1000)/10)**2))*np.cos(k*2*np.pi*1000*x11)*np.sin((k*np.pi*delta1)+np.arctan(-((k*1000)/10))) for k in range(1, n, 1))


delta2 = np.full(1, delta[2])
x22 = np.linspace(-2/1000, 2/1000,2000)
y2 = delta2 + sum((2/(k*np.pi))*np.cos(k*2*np.pi*1000*x22)*np.sin((k*np.pi*delta2)) for k in range(1, n, 1))
y22 = delta2 + sum((2/(k*np.pi))*(1/np.sqrt(1+((k*1000)/10)**2))*np.cos(k*2*np.pi*1000*x22)*np.sin((k*np.pi*delta2)+np.arctan(-((k*1000)/10))) for k in range(1, n, 1))


delta3 = np.full(1, delta[3])
x33 = np.linspace(-2/1000, 2/1000,2000)
y3 = delta3 + sum((2/(k*np.pi))*np.cos(k*2*np.pi*1000*x33)*np.sin((k*np.pi*delta3)) for k in range(1, n, 1))
y33 = delta3 + sum((2/(k*np.pi))*(1/np.sqrt(1+((k*1000)/10)**2))*np.cos(k*2*np.pi*1000*x33)*np.sin((k*np.pi*delta3)+np.arctan(-((k*1000)/10))) for k in range(1, n, 1))


delta4 = np.full(1, delta[4])
x44 = np.linspace(-2/1000, 2/1000,2000)
y4 = delta4 + sum((2/(k*np.pi))*np.cos(k*2*np.pi*1000*x44)*np.sin((k*np.pi*delta4)) for k in range(1, n, 1))
y44 = delta4 + sum((2/(k*np.pi))*(1/np.sqrt(1+((k*1000)/10)**2))*np.cos(k*2*np.pi*1000*x44)*np.sin((k*np.pi*delta4)+np.arctan(-((k*1000)/10))) for k in range(1, n, 1))



delta5 = np.full(1, delta[5])
x55 = np.linspace(-2/1000, 2/1000,2000)
y5 = delta5 + sum((2/(k*np.pi))*np.cos(k*2*np.pi*1000*x55)*np.sin((k*np.pi*delta5)) for k in range(1, n, 1))
y55 = delta5 + sum((2/(k*np.pi))*(1/np.sqrt(1+((k*1000)/10)**2))*np.cos(k*2*np.pi*1000*x55)*np.sin((k*np.pi*delta5)+np.arctan(-((k*1000)/10))) for k in range(1, n, 1))

plt.subplot(3, 2, 1)
plt.plot(x00, y0, color="lightblue")
plt.plot(x00, y00, color="red")

plt.subplot(3, 2, 2)
plt.plot(x11, y1, color="lightblue")
plt.plot(x11, y11, color="red")

plt.subplot(3, 2, 3)
plt.plot(x22, y2, color="lightblue")
plt.plot(x22, y22, color="red")
plt.ylabel("[un. arb.]", fontsize = "x-large")

plt.subplot(3, 2, 4)
plt.plot(x33, y3, color="lightblue")
plt.plot(x33, y33, color="red")

plt.subplot(3, 2, 5)
plt.plot(x44, y4, color="lightblue")
plt.plot(x44, y44, color="red")
plt.xlabel('Time [s]', fontsize = "x-large")

plt.subplot(3, 2, 6)
plt.plot(x55, y5, color="lightblue")
plt.plot(x55, y55, color="red")
plt.xlabel('Time [s]', fontsize = "x-large")

plt.show()