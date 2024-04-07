import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Lista dei nomi dei file di dati
nomi_file = ["./es11/data_6_4.txt", "./es11/data_10_1.txt", "./es11/data_12_2.txt", "./es11/data_15_1.txt", "./es11/data_17_6.txt"]

# Creazione della griglia di 5x2 immagini
fig, axs = plt.subplots(5, 2, figsize=(15, 20))

# Iterazione sulla griglia per tracciare ogni immagine
for i, nomefile in enumerate(nomi_file):
    x, y = np.loadtxt(nomefile, unpack=True)
    
    # Indice per posizionare il grafico nella griglia 5x2
    row = i
    col = 0
    
    # Tracciamento del segnale nel dominio del tempo
    axs[row, col].plot(x, y)
    axs[row, col].tick_params(axis='both', which='major', labelsize=12)
    
    # Calcolo della trasformata di Fourier
    ASD = abs(np.fft.rfft(y))
    numpunti = int(len(y) / 2) + 1
    risfreq = 1 / (1e-6 * max(x))
    freqmax = numpunti * risfreq
    freq = np.linspace(0, freqmax, numpunti)
    
    # Tracciamento dello spettro di potenza nel dominio delle frequenze
    axs[row, col + 1].plot(freq, ASD, color="red")
    axs[row, col + 1].tick_params(axis='both', which='major', labelsize=12)
    
    # Impostazione dei limiti dell'asse x per la colonna di destra
    axs[row, col + 1].set_xlim(0, 3000)
   
    # Trova i picchi nelle ASD
    peaks, _ = find_peaks(ASD, height=10100)
    
    # Aggiungi un testo per ogni picco trovato
    for peak in peaks:
        axs[row, col + 1].text(freq[peak], ASD[peak], f'{freq[peak]:.0f} Hz', fontsize=8, ha='center', va='bottom', rotation=45)

    # Aggiunta della legenda
    if i == 0:
        axs[row, col].legend(["Alluminio pieno"], loc='upper right', handlelength=0)
        axs[row, col + 1].legend(["Alluminio pieno"], loc='upper right', handlelength=0)
        axs[row, col + 1].set_yscale("log")
    elif i == 1:
        axs[row, col].legend(["Alluminio segato"], loc='upper right', handlelength=0)
        axs[row, col + 1].legend(["Alluminio segato"], loc='upper right', handlelength=0)
        axs[row, col + 1].set_yscale("log")        
    elif i == 2:
        axs[row, col].legend(["Ferro pieno"], loc='upper right', handlelength=0)
        axs[row, col + 1].legend(["Ferro pieno"], loc='upper right', handlelength=0)
        axs[row, col + 1].set_yscale("log")        
    elif i == 3:
        axs[row, col].legend(["Ferro laminato"], loc='upper right', handlelength=0)
        axs[row, col + 1].legend(["Ferro laminato"], loc='upper right', handlelength=0)
        axs[row, col + 1].set_yscale("log")
    elif i == 4:
        axs[row, col].legend(["Ottone pieno"], loc='upper right', handlelength=0)
        axs[row, col + 1].legend(["Ottone pieno"], loc='upper right', handlelength=0)
        axs[row, col + 1].set_yscale("log")


fig.supylabel('Signal [digit]')
fig.text(0.5, 0.5, 'ASD [arb.un.]', va='center', rotation='vertical', fontsize=14)
fig.text(0.25, 0.005, 'Time [$\mu$s]', va='center', rotation='horizontal', fontsize=14)
fig.text(0.75, 0.005, 'Frequency [Hz]', va='center', rotation='horizontal', fontsize=14)

# Regolazione del layout e visualizzazione della griglia di immagini
plt.tight_layout()
plt.savefig("auto-osc.pdf")
plt.show()
