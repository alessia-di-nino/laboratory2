import numpy as np
import matplotlib.pyplot as plt


def fourier_series_square(t, frequency, amplitude, num_terms):
    result = []
    for current_t in t:
        term = 0
        for k in range(1, num_terms + 1):
            bk = 0 if k%2 == 0 else (2/(k * np.pi))**2 
            term += bk * np.cos(k * frequency * current_t)
        result.append(term)
        
    return result

# Parametri della forma d'onda quadra
frequency = 10.0  # Frequenza della forma d'onda in Hertz
amplitude = 1.0  # Ampiezza della forma d'onda


num_term = 100
intervals = [10, 20, 50, 100, 500, 1000]

fig, axs = plt.subplots(3, 2)

for i, interval in enumerate(intervals):
    t = np.linspace(0, 2, interval, endpoint=False)

    res = fourier_series_square(t, frequency, amplitude, num_term)
   
    line, = axs[i%3, i//3].plot(t, res, label=f'x = {interval}')
    axs[i % 3, i // 3].legend(handles=[line], handlelength=0)


plt.show()

