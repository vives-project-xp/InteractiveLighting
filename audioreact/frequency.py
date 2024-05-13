import pyaudio
import numpy as np
import time
import matplotlib.pyplot as plt

# Constants
CHUNK_SIZE = 1024  # Number of frames per buffer
FORMAT = pyaudio.paInt16
CHANNELS = 1  # Mono audio
RATE = 44100  # Sampling rate in Hz

# Define frequency bands with logarithmic scaling
FREQUENCY_BANDS = {
    'Sub-bass': (16, 60),
    'Bass': (60, 250),
    'Low mids': (250, 500),
    'Mids': (500, 2000),
    'High mids': (2000, 4000),
    'Presence': (4000, 6000),
    'Brilliance': (6000, 16000)
}

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
bars = ax.bar(FREQUENCY_BANDS.keys(), np.zeros(len(FREQUENCY_BANDS)), align='center')
ax.set_ylabel('Magnitude (dB)')
ax.set_title('Realtime Audio Equalizer')
ax.set_ylim(0, 100)  # Adjust y-axis limit as needed

# Start updating plot
plt.show()

try:
    while True:
        # Read audio data from the stream
        data = stream.read(CHUNK_SIZE, exception_on_overflow=False)
        # Convert binary data to numpy array
        audio_signal = np.frombuffer(data, dtype=np.int16)

        # Apply FFT (Fast Fourier Transform) to get frequency spectrum
        fft_result = np.fft.fft(audio_signal)
        # Frequency bins corresponding to FFT result
        freq_bins = np.fft.fftfreq(len(fft_result), 1.0 / RATE)

        # Calculate magnitude of each frequency band
        band_magnitudes = {}
        for band, (low_freq, high_freq) in FREQUENCY_BANDS.items():
            low_idx = np.where(freq_bins >= low_freq)[0][0]
            high_idx = np.where(freq_bins >= high_freq)[0][0]
            band_mag = np.sum(np.abs(fft_result[low_idx:high_idx])) / CHUNK_SIZE
            # Apply logarithmic scaling
            band_mag_log = ((10 * np.log10(band_mag + 1))**2)/23
            band_magnitudes[band] = band_mag_log

        # Update plot
        for i, (band, mag) in enumerate(band_magnitudes.items()):
            bars[i].set_height(mag)
        fig.canvas.draw()
        fig.canvas.flush_events()

        # Add half-second delay
     

except KeyboardInterrupt:
    print("Exiting...")

# Close the audio stream
stream.stop_stream()
stream.close()

# Terminate PyAudio
p.terminate()
