var express = require("express");
var app = express();
var cookieparser = require('cookie-parser');
var session = require('express-session');
var csrf = require('csurf');
bodyparser = require('body-parser');
var cookieparser= require('cookie-parser'); 

//cookieparser must be placed before csrf 
app.use(bodyparser.urlencoded({extended:false}));
app.use(cookieparser('randomStringisHere222'));
// app.use(csrf({cookie:{key:XSRF-TOKEN,path:'/'}}));

//add the your app routes here
// app.use("/api", person);
// app.use("/", home);

 app.get("/", function(req, res) {
 	res.render('login2.html',{csrfTokenFromServer:req.csrfToken()});
    // res.sendfile('login2.html')
    // res.render('login_form', { csrf: req.csrfToken() });
 	// res.cookie('XSRF-TOKEN', req.csrfToken());
 });

  app.post("/user/add", function(req, res) { 
	/* some server side logic */
	res.send("OK");
  });

 /* serves all the static files */
 app.get(/^(.+)$/, function(req, res){ 
     console.log('static file request : ' + req.params);
     res.sendfile( __dirname + req.params[0]); 
 });

 var port = process.env.PORT || 8081;
 app.listen(port, function() {
   console.log("Listening on " + port);
 });