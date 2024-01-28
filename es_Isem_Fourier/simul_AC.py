import numpy as np
import matplotlib.pyplot as plt

# Parametri dell'onda quadra
frequenza = 50  # Hz
ampiezza = 1.0
durata = 1.0  # secondi
campionamento = 1000  # numero di campioni per secondo

# Generazione dell'onda quadra
tempo = np.linspace(0, durata, int(durata * campionamento), endpoint=False)
onda_quadra = ampiezza * np.sign(np.sin(2 * np.pi * frequenza * tempo))

# Trasformazione dei tratti verticali in tratti esponenziali
tratti_esponenziali = np.exp(-tempo)
onda_esponenziale = onda_quadra * tratti_esponenziali

# Plot dell'onda quadra con tratti esponenziali
plt.plot(tempo, onda_esponenziale)
plt.title('Onda Quadra con Tratti Esponenziali')
plt.xlabel('Tempo (s)')
plt.ylabel('Ampiezza')
plt.grid(True)
plt.show()