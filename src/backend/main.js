const express = require('express');
const mqtt = require('./mqtt.js');
const app = express();
const port = 3000;
const cors = require('cors');
app.use(
    cors({
            origin:"http://localhost:3000",
            optionsSuccessStatus:200
    })
)
app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
app.use(express.json());
app.get('/', (req, res) => {
  res.send('Hello World!');
});
app.get('/effect', (req, res) => {
  res.send('Effect: ' + req.query.effect);
});
app.post('/onof', (req,res) =>{
  try {
    mqtt.publish('IL/api', "{'on':" + req.body.on + "}");
    res.send('Onof published successfully');
  } catch (error) {
    console.error(error);
    res.status(500).send('Error publishing onof');
  } });


app.post('/effect', (req, res) => {
  try {
    mqtt.publish('IL/effect', req.body.effect);
    res.send('Effect published successfully');
  } catch (error) {
    console.error(error);
    res.status(500).send('Error publishing effect');
  }
});