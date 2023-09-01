const mongoose = require("mongoose");

const productSchema = new mongoose.Schema({
  name: { type: String, required: true },
  price: { type: Number, required: true },
  description: String,
  createAt: { type: Date, default: Date.now },
});

module.exports = mongoose.model("Product", productSchema);
