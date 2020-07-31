class ChessBoard {
    constructor(name) {
        this.name = name;
        this.grid = this.setup();
    }

    setup() {
        let board = new Array(8);
        for(let i=0; i < board.length; i++){
            board[i] = new Array(8);
        }
        return board
    }
}

export {ChessBoard};