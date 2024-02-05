import numpy as np
import matplotlib.pyplot as plt

'''
t = np.linspace(-2, 2, 1000)


def fourier_series_square(t, frequency, amplitude, num_terms):
    result = []
    for current_t in t:
        term = 0
        for k in range(1, num_terms + 1):
            ck = 0 if k%2 == 0 else 2/(k * np.pi) 
            term += ck * np.sin(k * frequency * current_t)
        result.append(term)
        
    return result

def HPF(t, frequency, amplitude, num_terms):
    result = []
    for current_t in t:
        term = 0
        for k in range(1, num_terms + 1):
            ck = 0 if k%2 == 0 else 2/(k * np.pi) 
            term += (ck * np.sin((k * frequency * current_t)+ np.arctan(1/5))* (1/np.sqrt(1+1/25)))
        result.append(term)
        
    return result

# Parametri della forma d'onda quadra
frequency = 5.0  # Frequenza della forma d'onda in Hertz
amplitude = 1.0  # Ampiezza della forma d'onda
num_terms = 10000


fig = plt.figure()

result = fourier_series_square(t, frequency, amplitude, num_terms)
result1 = HPF(t, frequency, amplitude, num_terms)
plt.plot(t,result, color = "lightblue")
plt.plot(t, result1, color = "red")
plt.show()
'''
fig = plt.figure()
n = 1000
xs = np.linspace(-2, 2, 1000)
frequency = 40

y = []
y1 = []

for x in xs:
    y.append(sum( [   2/(k * np.pi)*(k%2) * np.sin(k * frequency * x) for k in range(1, n, 1)    ]    )  )

    y1.append(sum( [ (2/(k * np.pi)*(k%2) * np.sin((k * frequency * x)+ np.arctan(1/4)))* (1/np.sqrt(1+1/16)) for k in range(1, n, 1) ] ))

plt.plot(xs,y)
plt.plot(xs, y1, color = "red")
plt.show()


