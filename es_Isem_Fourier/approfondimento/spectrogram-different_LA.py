import librosa
import matplotlib.pyplot as plt

# Define paths to audio files
audio_paths = [
    './es_Isem_Fourier/approfondimento/guitar/guitar_B2_very-long_forte_normal.mp3',
    './es_Isem_Fourier/approfondimento/guitar/guitar_B3_very-long_piano_normal.mp3',
    './es_Isem_Fourier/approfondimento/guitar/guitar_B4_very-long_forte_normal.mp3',
    './es_Isem_Fourier/approfondimento/guitar/guitar_B5_very-long_piano_harmonics.mp3'

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
        ax.set_title('B2')
    elif i == 1:
        ax.set_title('B3')
    elif i == 2:
        ax.set_title('B4')
    elif i == 3:
        ax.set_title('B5')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
