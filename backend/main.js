const express = require('express'), bodyParser = require("body-parser"),
swaggerJsdoc = require("swagger-jsdoc"),
swaggerUi = require("swagger-ui-express");;
//const swaggerDocument = require('./router/swagger.yaml');
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
              url: process.env.VITE_BACKEND_URL,
          },
      ],
  },
  apis: ["router/swagger.yaml"],
};
// Middleware setup
app.use(cors({
  origin: "*",
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
