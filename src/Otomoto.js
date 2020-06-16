const mongoose = require("mongoose");
const Schema = mongoose.Schema;
// create Otomoto Schema & model
// Schema
const OtomotoSchema = new Schema({
  brand: {
    type: String,
  },

  model: {
    type: String,
  },

  year: {
    // year
    type: String,
  },
  mileage: {
    //  migeagle
    type: String,
  },
  capacity: {
    type: String,
  },
  fuel_type: {
    type: String,
  },
  horse_power: {
    type: String,
  },
  transmission: {
    type: String,
  },
  type: {
    type: String,
  },
  number_of_doors: {
    type: String,
  },
  color: {
    type: String,
  },
  price: {
    type: String,
  },
  price_currency: {
    type: String,
  },
  features: {
    type: String,
  },
  url: {
    type: String,
  },
  number: {
    type: String
  }
});
// Model represents the collection in the data base
// allegro will be a collection in the db
const Otomoto = mongoose.model("otomoto", OtomotoSchema);
// allegro will get plurised so allegros is the collection
module.exports = Otomoto;
