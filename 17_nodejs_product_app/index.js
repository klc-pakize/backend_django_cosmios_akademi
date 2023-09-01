const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");

const productRouter = require("./src/router/productRouter");

const app = express();

app.use(bodyParser.json());
app.use(productRouter);

const username = "cosmiospakize";
const password = "q0nWYieLFdEWrUj1";
const databaseName = "products";

// q0nWYieLFdEWrUj1

mongoose
  .connect(
    `mongodb+srv://${username}:${password}@cluster0.rkkatwl.mongodb.net/${databaseName}?retryWrites=true&w=majority`
  )
  .then(() => {
    console.log("Connected to database");
  })
  .catch((error) => {
    console.log(error);
  });

app.listen(5000, () => {
  console.log("Server 5000 portunda çalıyor..");
});
