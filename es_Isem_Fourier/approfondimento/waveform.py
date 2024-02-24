import librosa
import librosa.display
import matplotlib.pyplot as plt

def plot_audio_waveform(audio_file):
    # Load the audio file
    y, sr = librosa.load(audio_file)

    # Plot the waveform
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(y, sr=sr)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.title("Waveform of {}".format(audio_file))
    plt.show()

# Example usage
audio_file = "./es_Isem_Fourier/approfondimento/guitar/guitar_A2_very-long_forte_normal.mp3"  # Replace with your MP3 file
plot_audio_waveform(audio_file)

plt.show()