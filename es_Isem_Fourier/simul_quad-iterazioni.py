import numpy as np
import matplotlib.pyplot as plt


def fourier_series_square(t, frequency, amplitude, num_terms):
    result = []
    for current_t in t:
        term = 0
        for k in range(1, num_terms + 1):
            ck = 0 if k%2 == 0 else 2/(k * np.pi) 
            term += ck * np.sin(k * frequency * current_t)
        result.append(term)
        
    return result

# Parametri della forma d'onda quadra
frequency = 5.0  # Frequenza della forma d'onda in Hertz
amplitude = 1.0  # Ampiezza della forma d'onda


t = np.linspace(-2, 2, 1000, endpoint=False)

num_terms = [1, 3, 5, 10, 50, 100, 500, 1000, 5000, 10000]


fig, axs = plt.subplots(5, 2)

for i, num_term in enumerate(num_terms):
   
    res = fourier_series_square(t, frequency, amplitude, num_term)
   
    line, = axs[i%5, i//5].plot(t, res, label=f'n = {num_term}')
    axs[i % 5, i // 5].legend(handles=[line], handlelength=0)

fig.supxlabel('Tempo [T]')
fig.supylabel('Segnale simulato [u.a.]')

plt.show()

