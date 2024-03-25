const mqtt = require("mqtt");
const url = "mqtt://mqtt.devbit.be:1883";
const options = {
  connectTimeout: 4000,
  username: "",
  password: "",
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