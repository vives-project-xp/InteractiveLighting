const express = require('express');
const router = require('./router/router.js');
const app = express();
const port = 3000;
const cors = require('cors');

// Middleware setup
app.use(cors({
  origin: "http://localhost:3000",
  optionsSuccessStatus: 200
}));
app.use(express.json()); // Parse JSON bodies

// Mount the router
app.use('/', router);

// Start the server
app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
