
import numpy as np
import matplotlib.pyplot as plt
import pyaudio
import mqtt from paho.mqtt.client as mqtt
# Parameters
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100
CHUNK = 1024
NUM_BANDS = 10
GAIN_RANGE = (0.5, 1.5) 

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

# Create bands
band_size = RATE // NUM_BANDS
gain_values = np.random.uniform(low=GAIN_RANGE[0], high=GAIN_RANGE[1], size=NUM_BANDS)

# Plot setup
plt.ion()
fig, ax = plt.subplots()
x = np.arange(0, NUM_BANDS)
bars = ax.bar(x, gain_values)
ax.set_ylim(0, 2)
ax.set_xticks(x)
ax.set_title('Equalizer')
ax.set_xlabel('Band')
ax.set_ylabel('Gain')

# Update function for live plotting
def update_plot(gain_values):
    for bar, val in zip(bars, gain_values):
        bar.set_height(val)
    fig.canvas.draw()
    fig.canvas.flush_events()

# Main loop
try:
    while True:
        data = stream.read(CHUNK)
        audio_signal = np.frombuffer(data, dtype=np.float32)
        equalized_audio = np.zeros_like(audio_signal)
        
        for i in range(NUM_BANDS):
            start = i * band_size
            end = start + band_size
            equalized_audio[start:end] = audio_signal[start:end] * gain_values[i]
        
        output_data = equalized_audio.astype(np.float32).tobytes()
        stream.write(output_data)
        update_plot(gain_values)
except KeyboardInterrupt:
    pass

# Close the stream and terminate PyAudio
stream.stop_stream()
stream.close()
p.terminate()
