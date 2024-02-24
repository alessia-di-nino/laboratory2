import librosa
import matplotlib.pyplot as plt

# Define paths to audio files
audio_paths = [
    './es_Isem_Fourier/approfondimento/guitar/guitar_A4_very-long_forte_normal.mp3',
    './es_Isem_Fourier/approfondimento/altri strumenti/banjo_A4_very-long_forte_normal.mp3',
    './es_Isem_Fourier/approfondimento/altri strumenti/violin_A4_05_mezzo-forte_arco-normal.mp3',
    './es_Isem_Fourier/approfondimento/altri strumenti/viola_A4_1_forte_arco-normal.mp3'
]

# Create a subplot for the four plots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Loop through each audio file and visualize its spectrogram
for i, (audio_path, ax) in enumerate(zip(audio_paths, axs.flatten())):
    x, sr = librosa.load(audio_path)
    X = librosa.stft(x)
    Xdb = librosa.amplitude_to_db(abs(X))
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz', ax=ax)
    ax.set_xlabel('Time')
    ax.set_ylabel('Frequency (Hz)')
    if i == 0:
        ax.set_title('Guitar Spectrogram')
    elif i == 1:
        ax.set_title('Banjo Spectrogram')
    elif i == 2:
        ax.set_title('Violin Spectrogram')
    elif i == 3:
        ax.set_title('Viola Spectrogram')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
