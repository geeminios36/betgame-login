var all = [];
for(i=1;i<=13;i++) {
    var firstCells = document.querySelectorAll('td:nth-child('+i+')');
    var cellValues = [];
    firstCells.forEach(function(singleCell) {
      cellValues.push(singleCell.innerText);
    });
    all.push(cellValues)
}

console.log(all.flat(1));
