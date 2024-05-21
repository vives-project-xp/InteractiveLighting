import pyaudio
import numpy as np
import time
import matplotlib.pyplot as plt
from scipy.ndimage import maximum_filter1d

# Constants
CHUNK_SIZE = 1024  # Number of frames per buffer
FORMAT = pyaudio.paInt16
CHANNELS = 1  # Mono audio
RATE = 44100  # Sampling rate in Hz
WINDOW_SIZE = 43  # Number of chunks to consider for BPM calculation
PEAK_THRESHOLD = 1.5  # Threshold for peak detection (adjust as necessary)

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK_SIZE)

# Initialize plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
ax.set_title('Realtime BPM Detection')
ax.set_ylim(0, 200)  # BPM range
bpm_text = ax.text(0.5, 0.5, '', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=30)

# Function to calculate BPM
def calculate_bpm(energy_buffer, rate):
    # Detect peaks
    peaks = maximum_filter1d(energy_buffer, size=3) == energy_buffer
    peak_indices = np.where(peaks & (energy_buffer > PEAK_THRESHOLD))[0]
    
    # Calculate intervals between peaks
    intervals = np.diff(peak_indices)
    
    # Calculate BPM
    if len(intervals) > 0:
        mean_interval = np.mean(intervals)
        bpm = 60.0 / (mean_interval * CHUNK_SIZE / rate)
    else:
        bpm = 0
    
    return bpm

# Energy buffer to store the energy values of the past WINDOW_SIZE chunks
energy_buffer = np.zeros(WINDOW_SIZE)

# Start updating plot
plt.show()

try:
    while True:
        # Read audio data from the stream
        data = stream.read(CHUNK_SIZE, exception_on_overflow=False)
        # Convert binary data to numpy array
        audio_signal = np.frombuffer(data, dtype=np.int16)
        
        # Calculate the energy of the current chunk
        energy = np.sum(audio_signal**2) / len(audio_signal)
        
        # Update energy buffer
        energy_buffer = np.roll(energy_buffer, -1)
        energy_buffer[-1] = energy
        
        # Calculate BPM
        bpm = calculate_bpm(energy_buffer, RATE)
        
        # Update plot
        bpm_text.set_text(f'BPM: {bpm:.2f}')
        fig.canvas.draw()
        fig.canvas.flush_events()
        
        # Add half-second delay
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Exiting...")

# Close the audio stream
stream.stop_stream()
stream.close()

# Terminate PyAudio
p.terminate()
