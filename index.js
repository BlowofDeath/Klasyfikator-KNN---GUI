const { app, BrowserWindow, Menu } = require('electron')

function createWindow () {
  // Stwórz okno przeglądarki.
  let win = new BrowserWindow({
    width: 1000,
    height: 700,
    webPreferences: {
      nodeIntegration: true
    },
    title: "Klasyfikator Knn",
    frame: true,
    icon: __dirname + '/logo.png'
  })

  // and load the index.html of the app.
  win.loadFile('index.html')
}

app.whenReady().then(function (){
  createWindow();
  const template = [ {
    label: 'File',
    submenu: [
      {
        role: 'quit'
      }
    ]
  }]
  const menu = Menu.buildFromTemplate(template)
  //Menu.setApplicationMenu(null);
})

app.on('window-all-closed', () => {
    // On macOS it is common for applications and their menu bar
    // to stay active until the user quits explicitly with Cmd + Q
    if (process.platform !== 'darwin') {
      app.quit()
    }
  })