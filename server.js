// server.js
const Otomoto = require("./src/Otomoto");
const express = require("express");
const app = express();
const connectDb = require("./src/connection");
const PORT = 5005;
// server.js
app.get("/scraping", async (req, res, next) => {
  res.send("Use /scraping/otomotos");
});
app.get("/scraping/:otomotos", async (req, res, next) => {
  try {
    //aritcles with null values

    const otomotos = await Otomoto.find();
    res.json(otomotos);
    //res.json(articles);
  } catch (err) {
    return res.status(422).send(err.message);
  }
});

app.listen(PORT, function () {
  console.log(`Listening on ${PORT}`);
  connectDb().then(() => {
    console.log("MongoDb connected");
  });
});
