import json

import paho.mqtt.client as mqtt

def send_json_to_mqtt_broker(json_string, topic, broker_address, broker_port):
    client = mqtt.Client()
    client.connect(broker_address, broker_port)
    client.publish(topic, json_string)
    client.disconnect()

# Example usage
json_string = json.dumps({"key": "value"})
topic = "my/topic"
broker_address = "mqtt.example.com"
broker_port = 1883

send_json_to_mqtt_broker(json_string, topic, broker_address, broker_port)