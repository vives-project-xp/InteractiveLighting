import pyaudio
import numpy as np
import time
import matplotlib.pyplot as plt
from madmom.features.onsets import peak_picking

# Constants
CHUNK_SIZE = 1024  # Number of frames per buffer
FORMAT = pyaudio.paInt16
CHANNELS = 1  # Mono audio
RATE = 44100  # Sampling rate in Hz

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
line, = ax.plot([], [])
ax.set_xlim(0, 60)  # Adjust x-axis limit as needed
ax.set_ylim(0, 300)  # Adjust y-axis limit as needed
ax.set_ylabel('Energy')
ax.set_title('Beat Detection (BPM)')
timestamps = []
energies = []

# Start updating plot
plt.show()

try:
    while True:
        # Read audio data from the stream
        data = stream.read(CHUNK_SIZE, exception_on_overflow=False)
        # Convert binary data to numpy array
        audio_signal = np.frombuffer(data, dtype=np.int16)

        # Calculate energy of the audio signal
        energy = np.sum(np.abs(audio_signal))

        # Append current timestamp and energy to lists
        timestamps.append(time.time())
        energies.append(energy)

        # Plot energy over time
        line.set_xdata(timestamps)
        line.set_ydata(energies)
        fig.canvas.draw()
        fig.canvas.flush_events()

        # Use Madmom's peak picking to detect onsets
        onsets = peak_picking(energies, threshold=0.2, pre_avg=0.1, post_avg=0.1, pre_max=0.3, post_max=0.3)
        if len(onsets) >= 2:
            # Calculate time difference between consecutive onsets
            time_diff = np.diff(onsets)
            # Calculate median time difference
            median_time_diff = np.median(time_diff)
            # Convert median time difference to BPM
            bpm = 60 / median_time_diff
            print(f"BPM: {bpm:.2f}")

        # Add half-second delay
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Exiting...")

# Close the audio stream
stream.stop_stream()
stream.close()

# Terminate PyAudio
p.terminate()
