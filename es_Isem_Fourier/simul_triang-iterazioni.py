import numpy as np
import matplotlib.pyplot as plt


def fourier_series_triang(t, frequency, amplitude, num_terms):
    result = []
    for current_t in t:
        term = 0
        for k in range(1, num_terms + 1):
            bk = 0 if k%2 == 0 else (2/(k * np.pi))**2 
            term += bk * np.cos(k * frequency * current_t)
        result.append(term)
        
    return result

# Parametri della forma d'onda triangolare
frequency = 5.0  # Frequenza della forma d'onda in Hertz
amplitude = 1.0  # Ampiezza della forma d'onda


t = np.linspace(-2, 2, 1000, endpoint=False) 

num_terms = [1, 3, 5, 10, 50, 100]


fig, axs = plt.subplots(3, 2)

for i, num_term in enumerate(num_terms):
   
    res = fourier_series_triang(t, frequency, amplitude, num_term)
   
    line, = axs[i%3, i//3].plot(t, res, label=f'n = {num_term}')
    axs[i % 3, i // 3].legend(handles=[line], handlelength=0)

fig.supxlabel('Tempo [T]')
fig.supylabel('Segnale simulato [u.a.]')

plt.show()

