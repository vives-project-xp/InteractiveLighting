const express = require('express');
const effects = require('./effects.js');
const mqtt = require('./mqtt.js');

const router = express.Router();
const baseTopic = process.env.MQTT_BASE_TOPIC + '/api';

var ledpieces = 0;

router.get('/', (req, res) => {
  res.send('Hello World!');
});

router.post('/speed', (req, res) => {
  try {
    const speed = req.body.speed;
    const jsonPayload = { seg: [{ id: 0, sx: speed }] };
    mqtt.publish(baseTopic, JSON.stringify(jsonPayload));
    res.send('Speed published successfully');
  } catch (error) {
    console.error(error);
    res.status(500).send('Error publishing speed');
  }
});

router.post('/ledpieces', (req, res) => {
  try {
    ledpieces = req.body.ledpieces;
    var ledamount = ledpieces*4;
    const jsonPayload = { seg: [{start:0,stop:ledamount,len:ledamount }] };
    mqtt.publish(baseTopic, JSON.stringify(jsonPayload));
    res.send('Ledpieces published successfully');
  } catch (error) {
    console.error(error);
    res.status(500).send('Error publishing ledpieces');
  }
});

router.post('/onof', (req, res) => {
  try {
  
  mqtt.publish(baseTopic, "{'on':" + req.body.on + "}");
  res.send('Onof published successfully');
  } catch (error) {
  console.error(error);
  res.status(500).send('Error publishing onof');
  }
});

router.post('/color', (req, res) => {
  try {
    const hexColor = req.body.color;
    const rgbwColor = hexToRgbw(hexColor);
    const jsonPayload = { seg: [{ id: 0, col: [rgbwColor] }] };

    function hexToRgbw(hex) {
      // Convert hex to RGB
      const r = parseInt(hex.slice(1, 3), 16);
      const g = parseInt(hex.slice(3, 5), 16);
      const b = parseInt(hex.slice(5, 7), 16);

      // Convert RGB to RGBW
      const w = 0;
      const newR = r;
      const newG = g;
      const newB = b;

      return [newR, newG, newB, w];
    }
    mqtt.publish(baseTopic, JSON.stringify(jsonPayload));
    res.send('Color published successfully');
  } catch (error) {
    console.error(error);
    res.status(500).send('Error publishing color');
  }
});

router.post('/random', (req, res) => {
  try {
    const jsonPayload = { seg: [{ id: 0,  fx: "r" }] };
    mqtt.publish(baseTopic, JSON.stringify(jsonPayload));
    res.send('Random published successfully');
  } catch (error) {
    console.error(error);
    res.status(500).send('Error publishing random');
  }
});

router.post(/brightness/, (req, res) => {
  try {
    const brightness = req.body.brightness;
    const jsonPayload = {
      bri: brightness
    };
    mqtt.publish(baseTopic, JSON.stringify(jsonPayload));
    res.send('Brightness published successfully');
  } catch (error) {
    console.error(error);
    res.status(500).send('Error publishing brightness');
  }
});

router.post('/effect', (req, res) => {
  try {
  console.log(req.body);
  const effect = req.body;
  const jsonPayload = { seg: [{ id: 0, fx: effect.fx }] };
  mqtt.publish(baseTopic, JSON.stringify(jsonPayload));
  res.send('Effect published successfully');
  } catch (error) {
  console.error(error);
  res.status(500).send('Error publishing effect');
  }
});

router.get('/effect', (req, res) => {
  const effectList = effects.getEffects();
  res.send(effectList);
});

module.exports = router;


