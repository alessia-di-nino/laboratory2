import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment

# Load the MP3 file
file_path = './es_Isem_Fourier/approfondimento/guitar/guitar_A2_very-long_forte_normal.mp3'
try:
    audio = AudioSegment.from_mp3(file_path)
except FileNotFoundError:
    print("File not found.")

# Convert the audio to raw data
samples = np.array(audio.get_array_of_samples())

# Get the sample rate (frame rate) and duration
frame_rate = audio.frame_rate
duration = len(samples) / frame_rate

# Time axis for plotting
time = np.linspace(0, duration, num=len(samples))

# Plot the waveform
plt.figure(figsize=(10, 4))
plt.plot(time, samples, color='b')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Waveform of Sound')
plt.grid()
plt.show()
