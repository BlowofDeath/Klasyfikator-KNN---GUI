let {PythonShell} = require('python-shell');
const app = require('electron').remote.app
var path = require('path');
var fs = require('fs');

function getData(script_number) {

    let datafilepath = document.getElementById("datafile").files[0].path;

    let k = $('#k-input').val()
    let x = $('#x-input').val()
    let metric = $('select[name=metric] option').filter(':selected').val()
    

    // '/python/env/Scripts/python'
    
    let pythonpath = path.normalize(path.join(__dirname, '/python/python').replace('app.asar', 'app.asar.unpacked'))
    let scriptpath = path.normalize(path.join(__dirname,'/python-scripts').replace('app.asar', 'app.asar.unpacked'))
    let args = ['--datafilepath',datafilepath,'--scriptnumber',script_number, '--k',k,'--x',x, '--metric', metric]

    if(metric == "minkowski") {
      args.push('--p')
      p = $('#p-input').val()
      args.push(p)
    }
      
    
    console.log("DIr: ", __dirname)
    //work: pythonPath: 'D:/Projekty/Electron Gui/python/env/Scripts/python',
    var options = {
        mode: 'text',
        pythonPath: pythonpath,
        pythonOptions: ['-u'],
        // make sure you use an absolute path for scriptPath
        scriptPath: scriptpath,
        //args: [datafilepath, script_number, k, x, '--bar=to jest bar']
        args: args
      };


    let pyshell = new PythonShell('knn.py', options);
   
 
// sends a message to the Python script via stdin
    //pyshell.send('hello');
    
    pyshell.on('message', function (message) {
      // received a message sent from the Python script (a simple "print" statement)
      $("#data").prepend(message+'\n'+"<br />")
    });
    
    // end the input stream and allow the process to exit
    pyshell.end(function (err,code,signal) {
      if (err) throw err;//$("#errorlog").prepend("Błąd z plikiem lub wprowadzono dane w złym formacie<br />");
      console.log('The exit code was: ' + code);
      console.log('The exit signal was: ' + signal);
      console.log('finished');
});
    
}

function clearData() {
  $("#data").text("");
}

function saveData() {
  let data = $("#data").text();
  try { fs.writeFileSync('Klasyfikator KNN output.txt', data, 'utf-8'); }
  catch(e) { alert('Failed to save the file !'); }
}


