var express = require('express');
var app = express.Router();
var apiSample = require('./sample');

/* GET home page. */
app.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

app.use('/api/sample', apiSample);

module.exports = app;
