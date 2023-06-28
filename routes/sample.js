const { log } = require('console');
var express = require('express');
var router = express.Router();
const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;


router.get('/data', function (req, res) {
    var content = fs.readFileSync('./saving.html', 'utf8');
    const dom = new JSDOM(content, { resources: "usable", runScripts: "dangerously"})
    const document = dom.window.document;
    document.addEventListener('load', () => {
        var all = [];
        for (i = 1; i <= 13; i++) {
            var firstCells = document.querySelectorAll('td:nth-child(' + i + ')');
            var cellValues = [];
            firstCells.forEach(function (singleCell) {
                cellValues.push(singleCell.textContent);
            });
            all.push(cellValues)
        };
    
        res.json({ mode: 'unavailable', data: all.flat(1) });
    });
});


module.exports = router;
