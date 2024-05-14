require('dotenv').config();


const mqtt = require("mqtt");
const url = process.env.MQTT_BROKER + "/api";
const options = {
  
  connectTimeout: 4000,
  username: process.env.MQTT_USERNAME, 
  password: process.env.MQTT_PASSWORD
};
const client = mqtt.connect(url, options);
client.on("connect", function () {
  console.log("Connected to mqtt server!");
});

client.on("error", (error) => {
  console.error("connection failed", error);
});
client.on("reconnect", (error) => {
  console.error("reconnect failed", error);
});

const publish = (topic, message) => {
  console.log("Publishing to " + topic + ": " + message);
  client.publish(topic, message.toString()
  );
};

module.exports = {
  publish,
};