import numpy as np
import matplotlib.pyplot as plt

# Lista dei nomi dei file di dati
nomi_file = ["./es13/alluminio-pieno.txt", "./es13/alluminio-segato.txt", "./es13/ferro.txt", "./es13/ferro-laminato.txt", "./es13/ottone-pieno.txt"]

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
    axs[row, col + 1].set_xlim(0, 1000)
   
    
    # Aggiunta della legenda
    if i == 0:
        axs[row, col].legend(["Alluminio pieno"], loc='upper right', handlelength=0)
        axs[row, col + 1].legend(["Alluminio pieno"], loc='upper right', handlelength=0)
        axs[row, col + 1].set_ylim(0, 60000)
    elif i == 1:
        axs[row, col].legend(["Alluminio segato"], loc='upper right', handlelength=0)
        axs[row, col + 1].legend(["Alluminio segato"], loc='upper right', handlelength=0)
        axs[row, col + 1].set_ylim(0, 140000)
    elif i == 2:
        axs[row, col].legend(["Ferro pieno"], loc='upper right', handlelength=0)
        axs[row, col + 1].legend(["Ferro pieno"], loc='upper right', handlelength=0)
        axs[row, col + 1].set_ylim(0, 50000)
    elif i == 3:
        axs[row, col].legend(["Ferro laminato"], loc='upper right', handlelength=0)
        axs[row, col + 1].legend(["Ferro laminato"], loc='upper right', handlelength=0)
        axs[row, col + 1].set_ylim(0, 170000)
    elif i == 4:
        axs[row, col].legend(["Ottone pieno"], loc='upper right', handlelength=0)
        axs[row, col + 1].legend(["Ottone pieno"], loc='upper right', handlelength=0)
        axs[row, col + 1].set_ylim(0, 60000)


fig.supylabel('Signal [digit]')
fig.text(0.495, 0.5, 'ASD [arb.un.]', va='center', rotation='vertical', fontsize=14)
fig.text(0.25, 0.005, 'Time [$\mu$s]', va='center', rotation='horizontal', fontsize=14)
fig.text(0.75, 0.005, 'Frequency [Hz]', va='center', rotation='horizontal', fontsize=14)

# Regolazione del layout e visualizzazione della griglia di immagini
plt.tight_layout()
plt.savefig("osc-smorz_core.pdf")
plt.show()
