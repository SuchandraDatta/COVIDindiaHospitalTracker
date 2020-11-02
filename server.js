const http = require('http');
const url = require('url');
const path = require('path');
const fs = require('fs');

const mimeTypes = {
	"html": "text/html",
	"jpeg": "image/jpeg",
	"jpg": "image/jpg",
	"png": "image/png",
	"js": "text/javascript",
	"css": "text/css",
	"json":"text/json",
	"webp":"image/webp"
};

http.createServer(function(req, res){
	
	try
	{
	var uri = url.parse(req.url).pathname;//url.parse takes in a URL as argument and returns an object, each part of the URL is now a property of the returned object like uri.host, uri.pathname etc
	var fileName = path.join(process.cwd(), decodeURI(uri));
	console.log("File name ", fileName)
	//Use decodeURI as unescape is depreciated(source Mozilla docs) it converts string to a form taking into account the escape sequences like unescape('%u0107');  becomes "ć"
		console.log("path.extname", path.extname(fileName).split("."))//Array like ['' 'html']
		var mimeType = mimeTypes[path.extname(fileName).split(".")[1]];
		/*Code for python starts*/
		console.log(mimeType)
		if(uri=='/indexAngularJS.html')
		{
			var spawn=require('child_process').spawn;
			var Newprocess=spawn('python', ['./hospitalTrackerScrapingSite.py']);
			Newprocess.stdout.on('data', function(data) { 
				console.log(data.toString()); 
			}) 
			console.log("SUCCESSFULLY EXECUTED THE SCRIPT")
		}
		/*Code for python ends*/
		res.writeHead(200, {'Content-type': mimeType});

		var fileStream = fs.createReadStream(fileName);
		fileStream.pipe(res);
	}
	catch(Exception)
	{}
	

}).listen(1337);

