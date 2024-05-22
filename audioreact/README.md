# Realtime Audio Equalizer with MQTT Integration

This project implements a realtime audio equalizer that visualizes audio frequency bands and sends data to an MQTT broker. The equalizer uses PyAudio to capture audio, applies Fast Fourier Transform (FFT) to analyze the frequency spectrum, and updates a Matplotlib plot to display the magnitude of each frequency band. The magnitudes are also published to an MQTT broker as JSON payloads.

## Features
- Captures live audio input
- Analyzes audio frequency bands using FFT
- Visualizes frequency bands in realtime using Matplotlib
- Publishes frequency band data to an MQTT broker

## Requirements
- Python 3.x
- Tkinter
- PyAudio
- NumPy
- Matplotlib
- Paho-MQTT

## Installation
1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install the required libraries:
    ```sh
    pip install pyaudio numpy matplotlib paho-mqtt aubio
    ```

## Usage
1. Clone the repository or copy the code into a Python script file.
2. Run the script:
    ```sh
    python script_name.py
    ```
3. A GUI will prompt you to enter the MQTT broker information:
    - MQTT Broker Host
    - MQTT Broker Port
    - MQTT Username (optional)
    - MQTT Password (optional)
    - MQTT Topic
4. The equalizer will start capturing audio, visualizing the frequency bands, and publishing data to the specified MQTT broker.

## Code Explanation
### Constants
- `CHUNK_SIZE`: Number of frames per buffer
- `FORMAT`: Audio format (16-bit PCM)
- `CHANNELS`: Number of audio channels (mono)
- `RATE`: Sampling rate in Hz
- `MAX_LEDS`: Maximum number of LEDs per frequency band
- `MAX_DB`: Maximum dB value for LED scaling
- `FREQUENCY_BANDS`: Dictionary defining the frequency bands with logarithmic scaling
- `COLORS`: Dictionary defining the color for each frequency band

### Functions
- `get_mqtt_info()`: Prompts the user for MQTT broker information using a GUI.
- `on_close()`: Closes the application when the GUI window is closed.
- `calculate_led_count(magnitude, max_leds, max_db)`: Calculates the number of LEDs to light up based on the magnitude.

### Main Process
1. Prompt the user for MQTT broker information.
2. Initialize PyAudio and the MQTT client.
3. Open the audio stream and initialize the Matplotlib plot.
4. Enter a loop to continuously read audio data, process it with FFT, update the plot, and publish the data to the MQTT broker.
5. Handle graceful exit on keyboard interrupt.

## Example MQTT Payload
```json
{
  "seg": {
    "i": [
      0, 1, "FF0000",  // LED 1, ON
      2, 3, "000000",  // LED 2, OFF
      ...
    ]
  }
}
```

## Notes
- Ensure that your microphone is properly connected and configured.
- Adjust the `MAX_DB` value to match the expected range of audio signal magnitudes.
- The script will automatically exit on pressing `Ctrl+C`.

## Troubleshooting
- If you encounter issues with PyAudio installation, refer to the official [PyAudio documentation](https://people.csail.mit.edu/hubert/pyaudio/#downloads).
- If the GUI doesn't appear, ensure Tkinter is properly installed and working.

# Beat Detection and Light Control

This project extends the realtime audio equalizer by adding beat detection and light control capabilities. It uses the `aubio` library for beat detection and controls the brightness of lights via MQTT.

## Features
- Detects beats in live audio input
- Controls light brightness based on detected beats
- Provides a GUI for configuring MQTT settings and light brightness levels

## Requirements
- Python 3.x
- Tkinter
- PyAudio
- Aubio
- NumPy
- Paho-MQTT

## Installation
1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install the required libraries:
    ```sh
    pip install pyaudio numpy paho-mqtt aubio
    ```
3. Install Voicemeeter and configure the loopback function.
## Usage
1. Clone the repository or copy the code into a Python script file.
2. Run the script:
    ```sh
    python script_name.py
    ```
3. Enter the MQTT broker information and light brightness settings in the GUI.
4. Click the "Start" button to begin beat detection and light control.

## Code Explanation
### Constants
- `BUFFER_SIZE`: Number of frames per buffer
- `SAMPLE_RATE`: Sampling rate in Hz
- `DEFAULT_BRIGHTNESS_FLASH`: Default brightness for flash (0-255)
- `DEFAULT_BRIGHTNESS_NORMAL`: Default brightness for normal state (0-255)
- `DEFAULT_FLASH_DURATION`: Default duration for flash in seconds

### Functions
- `on_connect(client, userdata, flags, rc)`: Callback for MQTT connection.
- `connect_mqtt(broker, port, username, password)`: Connects to the MQTT broker.
- `flash_lights()`: Flashes the lights by sending brightness values to the MQTT broker.
- `beat_detection()`: Detects beats and triggers light flashes.
- `start_beat_detection()`: Starts the beat detection in a separate thread.

### GUI
1. Enter MQTT broker details.
2. Set the flash and normal brightness levels.
3. Set the flash duration.
4. Click "Start" to begin beat detection and light control.

## Troubleshooting
- If you encounter issues with Aubio installation, refer to the official [Aubio documentation](https://aubio.org/).
- Ensure your microphone is properly connected and configured.
- Adjust the `DEFAULT_FLASH_DURATION` to match the desired flash effect duration.
