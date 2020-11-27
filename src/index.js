const express = require('express')
const { spawn } = require('child_process');
const app = express()
const port = 3000
app.get('/mwtest', (req, res) => {
    var dataToSend;
    let start = Date.now();
    console.log("start", start);
    // spawn new child process to call the python script
    var imagePath = 'https://homepages.cae.wisc.edu/~ece533/images/fruits.png';
    var brightness = 70;
    const python = spawn('python', ['./src/autoContrast.py', imagePath, brightness]);
    // collect data from script
    python.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...', data.buffer);
        dataToSend = data.toString();
    });
    // in close event we are sure that stream from child process is closed
    python.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        // send data to browser
        res.send(dataToSend)
        let end = Date.now();
        // timestamp in milliseconds
        console.log("close", end);
        console.log(Math.floor((end - start) / 1000));
    });

})
app.listen(port, () => console.log(`App listening on port ${port}!`))