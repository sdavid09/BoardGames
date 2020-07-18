
class Board {
    constructor(name) {
        this.name = name;
        this.row = {'A': 0, 'B': 1, 'C': 2,'D': 3, 'E': 4, 'F': 5,'G': 6, 'H': 7}
        this.column = {1:7, 2:6, 3:5, 4:4, 5:3, 6:2, 7:1, 8:0}
        this.grid = this.setupGrid();
    }

    setupGrid() {
        let grid = []

        for(let i=0 ; i<8; i++){
            grid.push(new Array(8));
        }
        return grid;
    }
}

export {Board};