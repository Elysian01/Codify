const express = require("express");
const path = require("path");


const app = express();
app.use(express.static(__dirname + '/public'));
app.use('/favicon.ico', express.static('images/favicon.ico'));

// app.use(function(req, res, next) {
//   res.header("Access-Control-Allow-Origin", "*");
//   res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
//   next();
// });

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname + '/index.html'))
})


app.listen(2400, () => {
  console.log("Server started at port 2400");
  console.log("http://localhost:2400/");
});

