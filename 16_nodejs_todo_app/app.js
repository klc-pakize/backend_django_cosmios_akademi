const express = require("express");
require("dotenv").config();

const app = express();

const port = process.env.PORT || 5001;
console.log(process.env.PORT);

const todoRouter = require("./src/routers/todoRouter");

app.use(express.json());

app.use("/api", todoRouter);

app.get("/", (req, res) => {
  res.send("Hoşgeldiniz...");
});

app.listen(port, () => {
  console.log(`Server: ${port} portum çalışıyor..`);
});
