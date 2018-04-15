var express = require('express');
var router = express.Router();
var formidable = require('formidable');
var path = require('path');


router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

//POST method to upload
router.post('/upload', function(req, res) {
  	var form = new formidable.IncomingForm();
  
    form.parse(req);

    form.on('fileBegin', function (name, file){
    	if(file.name != ""){
    		file.path = path.join(__dirname, '../public/uploads/' + file.name);
	        
	        var spawn = require('child_process').spawn,
    		py    = spawn('python', ['compute_input.py']),
    		data = file.path,
    		dataString = '';

			py.stdout.on('data', function(data){
  				dataString += data.toString();
			});
			py.stdout.on('end', function(){
  				console.log('Sum of numbers=',dataString);
			});
			py.stdin.write(JSON.stringify(data));
			py.stdin.end();

			res.send({error: 0, result: dataString});
    	} else {
    		res.send({error: 1});
    	}
    });

    form.on('file', function (name, file){
    	if(file.name != ""){
	        console.log('Uploaded ' + file.name);
    	} else {
    		console.log("Upload failed");
    	}      
    });

});
module.exports = router;
