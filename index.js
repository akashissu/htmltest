const express = require('express');
const mongoose = require('mongoose');
const app = express();

mongoose.connect('mongodb://localhost:27017/clinic', { useNewUrlParser: true, useUnifiedTopology: true });

app.get('/', (req, res) => {
  res.send('API is running...');
});

app.listen(5000, () => {
  console.log('Server running on http://localhost:5000');
});
