class Piece {
    constructor(name, icon, attributes) {
        this.name = name;
        this.icon = icon;
        this.attributes = attributes;
    }
}

class Rook extends Piece {
    constructor(icon, attributes) {
        super("Rook");
        this.icon = icon;
        this.attributes = attributes;
    }
}

class Knight extends Piece {
    constructor(icon, attributes) {
        super("Knight");
        this.icon = icon;
        this.attributes = attributes;
    }
}

class Bishop extends Piece {
    constructor(icon, attributes) {
        super("Bishop");
        this.icon = icon;
        this.attributes = attributes;
    }
}

class Queen extends Piece {
    constructor(icon, attributes) {
        super("Queen");
        this.icon = icon;
        this.attributes = attributes;
    }
}

class King extends Piece {
    constructor(icon, attributes) {
        super("King");
        this.icon = icon;
        this.attributes = attributes;
    }
}

class Pawn extends Piece {
    constructor(icon, attributes) {
        super("Pawn");
        this.icon = icon;
        this.attributes = attributes;
    }
}

export {Piece, Rook, Knight, Bishop, Queen, King, Pawn};