const express = require('express');
const router = express.Router();
const mqtt = require('./mqtt.js');

router.post('/onof', (req, res) => {
  try {
    console.log(req.body);
    mqtt.publish('IL/api', "{'on':" + req.body.on + "}");
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
        mqtt.publish('IL/api', JSON.stringify(jsonPayload));
        res.send('Color published successfully');
    } catch (error) {
        console.error(error);
        res.status(500).send('Error publishing color');
    }
    }
);
router.post('/random', (req, res) => {
    try {
        const jsonPayload = { seg: [{ id: 0, on: "true", fx: "r" }] };
        mqtt.publish('IL/api', JSON.stringify(jsonPayload));
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
        mqtt.publish('IL/api', JSON.stringify(jsonPayload));
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
    const jsonPayload = { seg: [{ id: 0, on: "true", fx: effect.fx }] };
    mqtt.publish('IL/api', JSON.stringify(jsonPayload));
    res.send('Effect published successfully');
  } catch (error) {
    console.error(error);
    res.status(500).send('Error publishing effect');
  }
});

module.exports = router;
