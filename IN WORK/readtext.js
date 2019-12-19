var http = require('http');
var fs = require('fs')

var nastya = http.createServer(function(req,res) {
  console.log(" url страницы " + req.url)
  res.writeHead(200,{'Content-Type': 'text/plain; charset=utf-8'});
  res.end("лол эта фигня работает");
});
nastya.listen(3000,'127.0.0.1');
console.log("мы отслеживаем порт 3000");
