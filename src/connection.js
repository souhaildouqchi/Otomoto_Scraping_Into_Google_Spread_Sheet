// connection.js
const mongoose = require("mongoose");
const connection = "mongodb://localhost:27017/scraping";
const connectDb = () => {
  return mongoose.connect(connection, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    useCreateIndex: true,
  });
};
module.exports = connectDb;
