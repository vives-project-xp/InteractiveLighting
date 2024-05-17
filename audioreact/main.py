import pyaudio
import numpy as np
import time
from madmom.features.beats import RNNBeatProcessor

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

# Initialize beat processor
beat_processor = RNNBeatProcessor()

print("Realtime BPM Detection")

try:
    while True:
        # Read audio data from the stream
        data = stream.read(CHUNK_SIZE, exception_on_overflow=False)
        # Convert binary data to numpy array
        audio_signal = np.frombuffer(data, dtype=np.int16)

        # Compute beats per minute (BPM)
        bpm = beat_processor(audio_signal, fps=RATE)

        # Display BPM
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