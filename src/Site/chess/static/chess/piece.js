class Piece {
    constructor(name, icon, color) {
        this.name = name;
        this.icon = icon;
        this.color = color;
    }
}

class Rook extends Piece {
    constructor(icon, color) {
        super("Rook");
        this.icon = icon;
        this.color = color;
    }
}

class Knight extends Piece {
    constructor(icon, color) {
        super("Knight");
        this.icon = icon;
        this.color = color;
    }
}

class Bishop extends Piece {
    constructor(icon, color) {
        super("Bishop");
        this.icon = icon;
        this.color = color;
    }
}

class Queen extends Piece {
    constructor(icon, color) {
        super("Queen");
        this.icon = icon;
        this.color = color;
    }
}

class King extends Piece {
    constructor(icon, color) {
        super("King");
        this.icon = icon;
        this.color = color;
    }
}

class Pawn extends Piece {
    constructor(icon, color) {
        super("Pawn");
        this.icon = icon;
        this.color = color;
    }
}

export {Piece, Rook, Knight, Bishop, Queen, King, Pawn};