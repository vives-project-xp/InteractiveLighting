import tkinter as tk
from tkinter import simpledialog
import pyaudio
import numpy as np
import time
import matplotlib.pyplot as plt
import json
import paho.mqtt.client as mqtt
import sys

# Constants
CHUNK_SIZE = 1024  # Number of frames per buffer
FORMAT = pyaudio.paInt16
CHANNELS = 1  # Mono audio
RATE = 44100  # Sampling rate in Hz
MAX_LEDS = 8  # Max number of LEDs per frequency band
MAX_DB = 50  # Maximum dB value for LED scaling

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

# Define colors for each frequency band
COLORS = {
    'Sub-bass': 'FF0000',  # Red
    'Bass': 'FF9300',      # Orange
    'Low mids': 'FFFF00',  # Yellow
    'Mids': '00FF00',      # Green
    'High mids': '0000FF', # Blue
    'Presence': 'F000FF',  # Indigo
    'Brilliance': 'FF0080' # Violet
}

def get_mqtt_info():
    """Prompt the user for MQTT broker information using a GUI."""
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.withdraw()  # Hide the root window

    broker_host = simpledialog.askstring("MQTT Broker", "Enter MQTT Broker Host:")
    if broker_host is None:
        return None
    broker_port = simpledialog.askinteger("MQTT Broker", "Enter MQTT Broker Port:")
    if broker_port is None:
        return None
    username = simpledialog.askstring("MQTT Broker", "Enter MQTT Username (optional):")
    if username is None:
        return None
    password = simpledialog.askstring("MQTT Broker", "Enter MQTT Password (optional):")
    if password is None:
        return None
    topic = simpledialog.askstring("MQTT Broker", "Enter MQTT Topic:")
    if topic is None:
        return None

    root.destroy()  # Destroy the root window
    return broker_host, broker_port, username, password, topic

def on_close():
    sys.exit()

# Get MQTT broker information from the user
mqtt_info = get_mqtt_info()
if mqtt_info is None:
    sys.exit()

MQTT_BROKER_HOST, MQTT_BROKER_PORT, MQTT_USERNAME, MQTT_PASSWORD, MQTT_TOPIC = mqtt_info

# Initialize PyAudio
p = pyaudio.PyAudio()

# Initialize MQTT Client
mqtt_client = mqtt.Client()
if MQTT_USERNAME and MQTT_PASSWORD:
    mqtt_client.username_pw_set(username=MQTT_USERNAME, password=MQTT_PASSWORD)
mqtt_client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT)

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
ax.set_ylim(0, MAX_DB)  # Adjust y-axis limit as needed

# Start updating plot
plt.show()

def calculate_led_count(magnitude, max_leds=MAX_LEDS, max_db=MAX_DB):
    """Calculate the number of LEDs to light up based on the magnitude."""
    led_count = int((magnitude / max_db) * max_leds)
    return min(max(led_count, 0), max_leds)

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
            band_mag_log = 10 * np.log10(band_mag + 1)
            band_magnitudes[band] = band_mag_log

        # Update plot
        for i, (band, mag) in enumerate(band_magnitudes.items()):
            bars[i].set_height(mag)
        fig.canvas.draw()
        fig.canvas.flush_events()

        # Prepare JSON payload for MQTT
        mqtt_payload = {
            "seg": {
                "i": []
            }
        }

        for i, (band, mag) in enumerate(band_magnitudes.items()):
            led_count = calculate_led_count(mag)
            color = COLORS[band]
            # Set LEDs for the current frequency band
            for j in range(MAX_LEDS):
                if j < led_count:
                    mqtt_payload["seg"]["i"].extend([i * MAX_LEDS + j, i * MAX_LEDS + j + 1, color])
                else:
                    mqtt_payload["seg"]["i"].extend([i * MAX_LEDS + j, i * MAX_LEDS + j + 1, '000000'])

        # Publish frequency band magnitudes to MQTT as JSON
        mqtt_client.publish(MQTT_TOPIC, json.dumps(mqtt_payload))

        # Add half-second delay
        time.sleep(0.02)

except KeyboardInterrupt:
    print("Exiting...")

# Close the audio stream
stream.stop_stream()
stream.close()

# Terminate PyAudio
p.terminate()

# Disconnect MQTT Client
mqtt_client.disconnect()
