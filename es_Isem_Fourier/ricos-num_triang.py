import numpy as np
import matplotlib.pyplot as plt

def triangular_waveform(t, frequency, amplitude):
    return amplitude * (2 / np.pi) * np.arcsin(np.sin(2 * np.pi * frequency * t) / np.pi)

def fourier_series_triangular(t, frequency, amplitude, num_terms):
    result = np.zeros_like(t)
    for n in range(1, num_terms + 1):
        harmonic = 2 * n - 1
        term = triangular_waveform(t, harmonic * frequency, amplitude) / harmonic
        result += term
    return result

# Parametri della forma d'onda triangolare
frequency = 1.0  # Frequenza della forma d'onda in Hertz
amplitude = 1.0  # Ampiezza della forma d'onda

# Parametri della serie di Fourier
num_terms = 100000  # Numero di termini nella serie di Fourier

# Creazione di un array di valori temporali
t = np.linspace(0, 2, 1000, endpoint=False)

# Calcolo della forma d'onda triangolare e della sua approssimazione tramite serie di Fourier
triangular_wave = triangular_waveform(t, frequency, amplitude)
fourier_approximation = fourier_series_triangular(t, frequency, amplitude, num_terms)

# Plot dei risultati
plt.figure(figsize=(10, 6))
plt.plot(t, triangular_wave, label='Forma d\'onda triangolare')
plt.plot(t, fourier_approximation, label=f'Approssimazione con {num_terms} termini')
plt.title('Ricostruzione numerica di una forma d\'onda triangolare tramite serie di Fourier')
plt.xlabel('Tempo (s)')
plt.ylabel('Ampiezza')
plt.legend()
plt.grid(True)
plt.show()