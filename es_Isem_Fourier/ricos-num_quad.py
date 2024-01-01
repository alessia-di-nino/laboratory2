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
num_terms1 = 1000  # Numero di termini nella serie di Fourier: studio in funzione del numero di iterazioni
num_terms2 = 5

'''
z = [1, 3, 5, 10, 50, 100, 500, 1000, 5000, 10000]
num_terms = z[0]
for i in z:
'''

# Creazione di un array di valori temporali
t = np.linspace(0, 2, 50, endpoint=False) #studio in funzione del campionamento: variare il numero di divisioni dell'aarray

# Calcolo della forma d'onda quadra e della sua approssimazione tramite serie di Fourier

fourier_approximation1 = fourier_series_square(t, frequency, amplitude, num_terms1)
fourier_approximation2 = fourier_series_square(t, frequency, amplitude, num_terms2)


# Plot dei risultati
plt.figure(figsize=(10, 6))
plt.plot(t, fourier_approximation1, label=f'Approssimazione con {num_terms1} termini')
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
'''
plt.show()

# 1) scrivere il ciclo for per inserire diversi valori di iterazioni senza ridefinire ogni volta la funzione in funzione di num_terms diversi
# 2) scrivere il codice fissando num_terms e variando il numero di suddivisioni dell'array di t (su x); unire in un unico codice i due studi diversi
    #(campionamento - cioè array - e troncamento - numero iterazioni della serie).