const http = require('http');
const url = require('url');
const path = require('path');
const fs = require('fs');
const utils = require('./utils/utils_for_template')
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
		if(uri=='/main.html')
		{
			let insert_data_in_template = ""

			var spawn=require('child_process').spawn;//Spawn a new process
			var Newprocess=spawn('python', ['./hospitalTrackerScrapingSite.py']);//Execute the python script for scraping
			Newprocess.stdout.on('data', function(data_from_python) { 
				//on receiving output from python where data_from_python is whatever python prints to console during processing, so if there are prints due to exceptions, they'll show up and cause a JSON parse error later on
				console.log("We got: ", data_from_python)
				if(data_from_python!=-1)
				{
					insert_data_in_template=data_from_python.toString()//This is the data from python containing array of JS objects
					file_contents=fs.readFile('main.html','utf-8', (err, data)=>{
					final_output = utils.augment_template(data, insert_data_in_template)//Custom code to inject the data_from_python into the main.html file
					res.writeHead(200, { 'Content-type': 'text/html'})
					res.write(final_output)
					return res.end()
					})
				//response.end() signals to the server that all headers and body has been sent, the server must consider the message to be complete. res.end() MUST BE CALLED at end of each response.
			    }
			    else
			    {
			    	res.writeHead(200, {"Content-type": "text/html"})
			    	fs.createReadStream("web_struct_upd_try_again_later.html").pipe(res)
			    }

			}) 
			console.log("SUCCESSFULLY EXECUTED THE SCRIPT")
		}
		else
		{
			//Execute this for requests for all other files such as image files.
			res.writeHead(200, {'Content-type': mimeType});
			var fileStream = fs.createReadStream(fileName);
			fileStream.pipe(res);
		}

	}
	catch(Exception)
	{}
	

}).listen(1337);
