import aubio
import pyaudio
import numpy as np
import paho.mqtt.client as mqtt
import json
import time
import tkinter as tk
import threading

# Constants
BUFFER_SIZE = 1024
SAMPLE_RATE = 44100
DEFAULT_BRIGHTNESS_FLASH = 255
DEFAULT_BRIGHTNESS_NORMAL = 0
DEFAULT_FLASH_DURATION = 0.2

# Initialize PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=SAMPLE_RATE,
                input=True,
                frames_per_buffer=BUFFER_SIZE)

# Initialize aubio's beat detection
beat_detector = aubio.tempo("default", BUFFER_SIZE, BUFFER_SIZE, SAMPLE_RATE)

# Set up MQTT client
client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with code {rc}")

client.on_connect = on_connect

def connect_mqtt(broker, port, username, password):
    if username and password:
        client.username_pw_set(username, password)
    client.connect(broker, int(port), 60)
    client.loop_start()

# Function to flash lights
def flash_lights():
    flash_message = json.dumps({"bri": brightness_flash.get()})
    client.publish(mqtt_topic.get(), flash_message)
    print("Lights flashed!")

    time.sleep(float(flash_duration.get()))

    normal_message = json.dumps({"bri": brightness_normal.get()})
    client.publish(mqtt_topic.get(), normal_message)
    print("Lights returned to normal brightness.")

# Beat detection function to be run in a separate thread
def beat_detection():
    global running
    connect_mqtt(mqtt_broker.get(), mqtt_port.get(), mqtt_username.get(), mqtt_password.get())

    print("Listening for beats...")
    try:
        while running:
            audio_data = stream.read(BUFFER_SIZE)
            audio_samples = np.frombuffer(audio_data, dtype=np.float32)

            is_beat = beat_detector(audio_samples)
            if is_beat:
                flash_lights()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
        client.loop_stop()
        client.disconnect()

# Start and stop functions for the beat detection thread
def start_beat_detection():
    global running
    running = True
    beat_thread = threading.Thread(target=beat_detection)
    beat_thread.start()


# Create main window
root = tk.Tk()
root.title("Beat Detection and Light Control")

# MQTT Settings
tk.Label(root, text="MQTT Broker:").grid(row=0, column=0)
mqtt_broker = tk.Entry(root)
mqtt_broker.grid(row=0, column=1)

tk.Label(root, text="MQTT Port:").grid(row=1, column=0)
mqtt_port = tk.Entry(root)
mqtt_port.grid(row=1, column=1)

tk.Label(root, text="MQTT Username:").grid(row=2, column=0)
mqtt_username = tk.Entry(root)
mqtt_username.grid(row=2, column=1)

tk.Label(root, text="MQTT Password:").grid(row=3, column=0)
mqtt_password = tk.Entry(root, show='*')
mqtt_password.grid(row=3, column=1)

tk.Label(root, text="MQTT Topic:").grid(row=4, column=0)
mqtt_topic = tk.Entry(root)
mqtt_topic.grid(row=4, column=1)

# Brightness Settings
tk.Label(root, text="Flash Brightness:").grid(row=5, column=0)
brightness_flash = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL)
brightness_flash.set(DEFAULT_BRIGHTNESS_FLASH)
brightness_flash.grid(row=5, column=1)

tk.Label(root, text="Normal Brightness:").grid(row=6, column=0)
brightness_normal = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL)
brightness_normal.set(DEFAULT_BRIGHTNESS_NORMAL)
brightness_normal.grid(row=6, column=1)

# Flash Duration
tk.Label(root, text="Flash Duration (s):").grid(row=7, column=0)
flash_duration = tk.Entry(root)
flash_duration.insert(0, DEFAULT_FLASH_DURATION)
flash_duration.grid(row=7, column=1)

# Start and Stop Buttons
start_button = tk.Button(root, text="Start", command=start_beat_detection)
start_button.grid(row=8, column=0, columnspan=2)

root.mainloop()
