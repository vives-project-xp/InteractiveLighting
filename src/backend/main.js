const express = require('express'), bodyParser = require("body-parser"),
swaggerJsdoc = require("swagger-jsdoc"),
swaggerUi = require("swagger-ui-express");;
const router = require('./router/router.js');
const app = express();
const port = 3000;
const cors = require('cors');
const options = {
  definition: {
      openapi: "3.1.0",
      info: {
          title: "Interactive Lighting API",
          version: "0.9.5",
          description:
              "This is the backend API for the Interactive Lighting project."
      },
      servers: [
          {
              url: "http://localhost:3000"
          },
      ],
  },
  apis: ["./router/router.js"],
};
// Middleware setup
app.use(cors({
  origin: "http://localhost:3000",
  optionsSuccessStatus: 200
}));
app.use(express.json()); // Parse JSON bodies

// Mount the router
app.use('/', router);
const specs = swaggerJsdoc(options);
app.use(
  "/api-docs",
  swaggerUi.serve,
  swaggerUi.setup(specs)
);

// Start the server
app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
