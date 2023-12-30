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
frequency = 10.0  # Frequenza della forma d'onda in Hertz
amplitude = 1.0  # Ampiezza della forma d'onda

# Parametri della serie di Fourier
num_terms1 = 1  # Numero di termini nella serie di Fourier
num_terms2 = 5

# Creazione di un array di valori temporali
t = np.linspace(0, 2, 1000, endpoint=False)

# Calcolo della forma d'onda quadra e della sua approssimazione tramite serie di Fourier

fourier_approximation1 = fourier_series_square(t, frequency, amplitude, num_terms1)
fourier_approximation2 = fourier_series_square(t, frequency, amplitude, num_terms2)

'''
# Plot dei risultati
plt.figure(figsize=(10, 6))
plt.plot(t, fourier_approximation, label=f'Approssimazione con {num_terms} termini')
plt.title('Ricostruzione numerica di una forma d\'onda quadra tramite serie di Fourier')
plt.xlabel('Tempo [T]')
plt.ylabel('Segnale simulato [u.a.]')
plt.legend()
plt.grid(True)
plt.show()
'''

fig, axs = plt.subplots(2)
axs[0].plot(t, fourier_approximation1)
axs[1].plot(t, fourier_approximation2)

plt.show()
