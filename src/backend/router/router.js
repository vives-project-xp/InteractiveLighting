const express = require('express');
const router = express.Router();
const effects = require('./effects.js');
const mqtt = require('./mqtt.js');


router.get('/', (req, res) => {
    res.send('Hello World!');
    }
);

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

router.get('/effect', (req, res) => {
  const effectList = effects.getEffects();
  res.send(effectList);
});
module.exports = router;

// vanaf hier de nodige docs voor swagger
/**
 * @swagger
 * tags:
 *   name: ILBackend
 *   description: This lists all the endpoints for the Interactive Lighting backend API
 * /:
 *   get:
 *     summary: Hello World
 *     description: With this you can check whether the backend is running
 *     responses:
 *       '200':
 *         description: Successful response
 *         schema:
 *           type: string
 *
 *
 * /onof:
 *   post:
 *     summary: Publish On/Off state
 *     description: Publishes the On/Off state of the lights to the MQTT broker
 *     parameters:
 *       - in: body
 *         name: on
 *         description: On/Off state
 *         required: true
 *         schema:
 *           type: object
 *           properties:
 *             on:
 *               type: boolean
 *     responses:
 *       '200':
 *         description: On/Off state published successfully
 *       '500':
 *         description: Error publishing On/Off state
 *
 * /color:
 *   post:
 *     summary: Publish color
 *     parameters:
 *       - in: body
 *         name: color
 *         description: Hex color code
 *         required: true
 *         schema:
 *           type: object
 *           properties:
 *             color:
 *               type: string
 *               format: color
 *           example: { "color": "#FF0000" }
 *     
 *     description: Publishes the color to the MQTT broker
 *     responses:
 *       '200':
 *         description: Color published successfully
 *       '500':
 *         description: Error publishing color
 *
 * /random:
 *   post:
 *     summary: Publish random effect
 *     responses:
 *       '200':
 *         description: Random effect published successfully
 *       '500':
 *         description: Error publishing random effect
 *
 * /brightness:
 *   post:
 *     summary: Publish brightness
 *     parameters:
 *       - in: body
 *         name: brightness
 *         description: Brightness value
 *         required: true
 *         schema:
 *           type: object
 *           properties:
 *             brightness:
 *               type: integer
 *     responses:
 *       '200':
 *         description: Brightness published successfully
 *       '500':
 *         description: Error publishing brightness
 *
 * /effect:
 *   post:
 *     summary: Publish effect
 *     parameters:
 *       - in: body
 *         name: fx
 *         description: Effect data
 *         required: true
 *         schema:
 *           type: object
 *           properties:
 *             fx:
 *               type: integer
 *     responses:
 *       '200':
 *         description: Effect published successfully
 *       '500':
 *         description: Error publishing effect
 *   get:
 *     summary: Get available effects
 *     responses:
 *       '200':
 *         description: Successful response
 *         schema:
 *           type: array
 *           items:
 *             type: string
 */
