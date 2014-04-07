
/**
 * Module dependencies.
 */

var express = require('express.io');
var http = require('http');
var path = require('path');
var billboard;
var i = require('readline').createInterface(process.stdin, process.stdout, null);

// Import API stuff
// var Rdio = require('./rdio').Rdio;
// var rdio = new Rdio({consumerKey:'es6qb4v7jezvr53ytrczreb7',consumerSecret:'r7xAyNYDav'});

var Rdio = require('rdio');
var rdio = new Rdio({rdio_api_key:"atf48dmcvw6rxa4jrhjh32wn",rdio_api_shared:"2hckahK7hF",callback_urlcallback_url:"http://localhost:3000/oauth/callback"})
var twilio = require('twilio')('ACec0c7c5211527b56dedd223ea469e3bc', 'a79b8b5c99c2cf699782fe2026cf1036');

var app = express();

// all environments
app.set('port', process.env.PORT || 3000);
app.use(express.favicon());
app.use(express.logger('dev'));
app.use(express.json());
app.use(express.urlencoded());
app.use(express.methodOverride());
app.use(express.static(path.join(__dirname, 'public'), '/'));

// development only
if ('development' == app.get('env')) {
  app.use(express.errorHandler());
}

app.listen(app.get('port'), function(){
   console.log("Express server listening on port " + app.get('port'));
});
// Authenticate against the Rdio service.
// rdio.beginAuthentication("oob", function (err, authUrl) {
// 	if (err) {
// 		console.log("ERROR1: " + require('util').inspect(err));
// 		return;
// 	}

// 	console.log("Go to: " + authUrl);

// 	// Prompt the user for the verifier code.
// 	i.question("Then enter the code: ", function (verifier) {
// 		rdio.completeAuthentication(verifier, function (err) {
// 			if (err) {
// 				console.log("ERROR: " + err);
// 				return;
// 			} r7xAyNYDav es6qb4v7jezvr53ytrczreb7
			rdio.api("h7f4tftm3k29nf6ccuph5dr4", "85k4jHCSnT", {
				'method'	: 'getObjectFromUrl',
				'url'		: 'http://www.rdio.com/people/Billboard/playlists/5087254/Billboard_Hot_100/',
				'extras'	: 'tracks'}, function(err, data) {
					if (err) {
						console.error("ERROR: "+require('util').inspect(err));
						return;
					}

					billboard = data.result;

					console.log(billboard);

					var memory = new Array(100);

					app.io.route('newvote', function(req) {
						var tempRand = [
							Math.floor(Math.random()*100),
							Math.floor(Math.random()*100),
							Math.floor(Math.random()*100),
							Math.floor(Math.random()*100)
						];
						while (rand[tempRand[0]] != true) {
							tempRand[0] = Math.floor(Math.random()*100)
						}
						while (rand[tempRand[1]] != true) {
							tempRand[1] = Math.floor(Math.random()*100)
						}
						while (rand[tempRand[2]] != true) {
							tempRand[2] = Math.floor(Math.random()*100)
						}
						while (rand[tempRand[3]] != true) {
							tempRand[3] = Math.floor(Math.random()*100)
						}
						req.io.broadcast('songs', [
							billboard["tracks"][tempRand[0]],
							billboard["tracks"][tempRand[1]],
							billboard["tracks"][tempRand[2]],
							billboard["tracks"][tempRand[3]]
						]);
					});
				// End rdio.call
			});

// 		});
// 	});
// });

