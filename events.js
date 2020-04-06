let {PythonShell} = require('python-shell');
const app = require('electron').remote.app
var path = require('path');

function getData(script_number) {

    let datafilepath = document.getElementById("datafile").files[0].path;

    let k = $('#k-input').val()
    let x = $('#x-input').val()
    console.log(app.getAppPath())
    console.log(path.normalize(__dirname))
    // '/python/env/Scripts/python'
    
    let pythonpath = path.normalize(path.join(__dirname, '/python/python').replace('app.asar', 'app.asar.unpacked'))
    console.log("Pypa: "+pythonpath)
    let scriptpath = path.normalize(path.join(__dirname,'/python-scripts').replace('app.asar', 'app.asar.unpacked'))
    
    console.log("DIr: ", __dirname)
    //work: pythonPath: 'D:/Projekty/Electron Gui/python/env/Scripts/python',
    var options = {
        mode: 'text',
        pythonPath: pythonpath,
        pythonOptions: ['-u'],
        // make sure you use an absolute path for scriptPath
        scriptPath: scriptpath,
        args: [datafilepath, script_number, k, x]
      };


    let pyshell = new PythonShell('knn.py', options);
   
 
// sends a message to the Python script via stdin
    //pyshell.send('hello');
    
    pyshell.on('message', function (message) {
      // received a message sent from the Python script (a simple "print" statement)
      $("#data").prepend(message+"<br />")
    });
    
    // end the input stream and allow the process to exit
    pyshell.end(function (err,code,signal) {
      if (err) $("#errorlog").prepend("Błąd z plikiem lub wprowadzono dane w złym formacie<br />");
      console.log('The exit code was: ' + code);
      console.log('The exit signal was: ' + signal);
      console.log('finished');
});
    
}

function clearData() {
  $("#data").text("");
}
