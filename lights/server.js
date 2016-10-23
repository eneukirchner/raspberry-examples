var express = require('express')
,   app = express()
,   server = require('http').createServer(app)
,   io = require('socket.io').listen(server)
,   conf = require('./config.json')
,   spawn = require('child_process').spawn
,   fs = require('fs');

var colors = { r:"0", g:"0", b:"0" };

// Webserver
// auf den Port x schalten
server.listen(conf.port);


// statische Dateien ausliefern
app.use(express.static(__dirname + '/public'));


// wenn der Pfad / aufgerufen wird
app.get('/', function (req, res) {
	// so wird die Datei index.html ausgegeben
	res.sendFile(__dirname + '/public/index.html');
});

// Websocket
io.sockets.on('connection', function (socket) {
    socket.emit('chat', colors);
    // console.log("Neuer Connect " + colors.r + ' ' + colors.g + ' ' +colors.b);
	// wenn ein Benutzer einen Text sendet
	socket.on('chat', function (data) {
		colors = data;
		// so wird dieser Text an alle anderen Benutzer gesendet
		console.log(new Date().toString() + ": " + colors.r + ' ' + colors.g + ' ' + colors.b);
		io.sockets.emit('chat', colors);
		var stream = fs.createWriteStream("buffer");
		stream.once('open', function(fd) {
			stream.write(colors.r + ':' + colors.g + ':' + colors.b);
			stream.end();
		});
	});
});

// Portnummer in die Konsole schreiben
console.log('Server listening on port ' + conf.port + '/');
