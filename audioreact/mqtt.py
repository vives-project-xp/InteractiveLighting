import json
import paho.mqtt.client as mqtt

# MQTT Broker details
MQTT_BROKER_HOST = "mqtt.devbit.be"
MQTT_BROKER_PORT = 1883
MQTT_USERNAME = ""
MQTT_PASSWORD = ""
MQTT_TOPIC = "IL"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
    else:
        print(f"Failed to connect, return code {rc}")
        
# Function to handle MQTT disconnection
def on_disconnect(client, userdata, rc):
    print("Disconnected from MQTT Broker")

# Function to publish JSON data to MQTT
def publish_json_to_mqtt(json_data):
    # Connect to MQTT Broker
    client = mqtt.Client()
    client.username_pw_set(username=MQTT_USERNAME, password=MQTT_PASSWORD)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT)
    client.loop_start()

    # Publish JSON data to MQTT topic
    client.publish(MQTT_TOPIC, json.dumps(json_data))

    # Disconnect from MQTT Broker
    client.loop_stop()
    client.disconnect()

# Input JSON data from command line
def input_json():
    json_input = input("Enter JSON data: ")
    try:
        json_data = json.loads(json_input)
        return json_data
    except ValueError:
        print("Invalid JSON format. Please enter valid JSON.")
        return None

# Main function
def main():
    json_data = input_json()
    if json_data:
        publish_json_to_mqtt(json_data)

if __name__ == "__main__":
    main()
