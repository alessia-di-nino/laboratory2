import numpy as np
import matplotlib.pyplot as plt

# Funzione per calcolare ASD (Absolute Sum of Differences) in kHz
def calculate_asd_kHz(x, y):
    fft_result = np.fft.rfft(y)
    asd = np.abs(fft_result)
    numpunti = int(len(y) / 2) + 1
    risfreq = 1 / (1e-6 * max(x))
    freqmax = numpunti * risfreq
    freq = np.linspace(0, freqmax / 1000, numpunti)  # Converti in kHz
    return freq, asd

# Trova i picchi di ASD
def find_peaks(freq, asd):
    peak_indices = np.where(asd > 0.8 * np.max(asd))[0]
    peak_freqs = freq[peak_indices]
    # Escludi lo zero dalle frequenze di picco
    peak_freqs = peak_freqs[peak_freqs > 0]
    return peak_freqs

# Caricamento dei dati e creazione dei grafici
fig, axs = plt.subplots(2, 1, figsize=(10, 6))

colors = ['tab:blue', 'tab:orange', 'tab:green']
capacitors = ['0.1 $\mu$F', '0.22 $\mu$F', '0.47 $\mu$F']

for i in range(1, 4):
    nomefile = f"./es12/c{i}.txt"
    x, y = np.loadtxt(nomefile, unpack=True)
    axs[0].plot(x, y, color=colors[i-1], label=f'C = {capacitors[i-1]}')
    freq, asd = calculate_asd_kHz(x, y)
    axs[1].plot(freq, asd, color=colors[i-1], label=f'C = {capacitors[i-1]}')
    peak_freqs = find_peaks(freq, asd)
    for peak_freq in peak_freqs:
        axs[1].text(peak_freq, 0.8 * np.max(asd), f'{peak_freq:.2f} kHz', ha='center', fontsize=8)

# Impostazioni per il primo grafico
axs[0].set_xlabel("time [$\mu$s]", fontsize=14)
axs[0].set_ylabel("signal [digit]", fontsize=14)
axs[0].set_title("Oscilloscope signals")
axs[0].legend()

# Impostazioni per il secondo grafico
axs[1].set_xlabel("frequency [kHz]", fontsize=14)
axs[1].set_ylabel("ASD [arb.un.]", fontsize=14)
axs[1].set_title("ASD")
axs[1].legend()

plt.tight_layout()
plt.show()

