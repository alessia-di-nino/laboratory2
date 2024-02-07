import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
n = 1000
xs = np.linspace(-2, 2, 1000)
frequency = 5

y = []
y1 = []

for x in xs:
    y.append(sum( [2/(k * np.pi)*(k%2) * np.sin(k * frequency * x) for k in range(1, n, 1)] ))

    y1.append(sum( [(2/(k * np.pi)*(k%2) * np.sin((k * frequency * x)+ np.arctan(1/4)))* (1/np.sqrt(1+1/16)) for k in range(1, n, 1)]))

plt.plot(xs, y, label='Onda quadra')
plt.plot(xs, y1, color="red", label='Distorsione')

# Adding labels to the axes
plt.xlabel('Tempo [T]')
plt.ylabel('Segnale simulato [u.a.]')

plt.legend()

plt.show()
