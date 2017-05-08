var http = require("http");
var fs = require('fs')
var url = require('url')
var Tokens =require('csrf')

//create a server
http.createServer(function (request, response)
	{
	
	//parse the request containing filename
	var pathname = url.parse(request.url).pathname;

	// print the name of the file for which request is made
	console.log("Request for "+ pathname + " required.");

	//read the request file	

	fs.readFile(pathname.substr(1), function (err, data)
	{

			if(err)
	        {
				// page not found
				console.log(err);
				response.writeHead(404,{'content-Type':'text/html'});
				
			}

			else
			{
				//page found
				response.writeHead(200,{'content-Type':'text/html'});
			
			// write the content of file to response body
				response.write(data.toString());
		    }
		//send response body

		response.end();
	});
	// response.end("<a href='login.html'>login</a>")

}).listen(8081);

console.log('Server running at http://127.0.0.1:8081/login.html')

