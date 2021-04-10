const express = require('express');
const app = express();
const port = process.env.PORT || 5000;
const fs = require('fs');
const { spawn } = require('child_process');

app.get('/', (req, res) => {
    fs.readFile('./view/index.html', function (err, data) {
        res.write(data);
    })

})

app.get('/plot', (req, res) => {
    const childPython = spawn('python', ["main.py"]);
    childPython.stdout.on('data', (data) => {
        console.log(data);
    })
    childPython.stderr.on('data', (data) => {
        console.log(data);
    })
});

app.listen(port, () => console.log(`Listening on port ${port}`));