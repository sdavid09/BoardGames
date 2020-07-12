import { Piece, Rook } from "./piece.js"
let pc = new Rook;
console.log(pc.icon);
console.log("nEW");

function addFirstPlayerPieces() {
    let piece_row = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1']
    let pieces = ['\u2656', '\u2658', '\u2657', '\u2655', '\u2654', '\u2657','\u2658', '\u2656']
    piece_row.forEach((element, index)=>{
        let piece = document.querySelector(`#${element}`)
        piece.classList.add("player-one-pieces")
        piece.textContent=`${pieces[index]}`
    })

    let pawns_row = ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2']
    pawns_row.forEach(element => {
       let pawn = document.querySelector(`#${element}`)
        pawn.classList.add("player-one-pieces")
        pawn.textContent = '\u2659'; 
    });
}
function addSecondPlayerPieces() {
    let piece_row = ['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8']
    let pieces = ['\u265C', '\u265E', '\u265D', '\u265B', '\u265A', '\u265D','\u265E', '\u265C']
    piece_row.forEach((element, index)=>{
       let piece = document.querySelector(`#${element}`)
        piece.classList.add("player-two-pieces")
        piece.textContent=`${pieces[index]}`
    })

    let pawns_row = ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7']
    pawns_row.forEach(element => {
      let pawn = document.querySelector(`#${element}`)
        pawn.classList.add("player-two-pieces")
        pawn.textContent = '\u265F'; 
    });
}
addFirstPlayerPieces();
addSecondPlayerPieces()

let table = document.querySelector("table")
let firstPick = false;
let secondPick;
let turn = false;

table.addEventListener("click", function(e){

    if(event.target.matches('td') && !turn && !firstPick && event.target.textContent.length){
       let all_classes = event.target.classList
       let player_class = all_classes[1]
        firstPick = {"icon" : event.target.textContent,
                    "class": player_class,
                    "element": event.target}
        turn = true;
    }
    else if (event.target.matches('td') && turn && firstPick ) { 
        if(event.target.textContent !== firstPick["element"].textContent){
            let all_classes = event.target.classList
            if( all_classes.length > 1 ){
                event.target.classList.remove(all_classes[1])
            }
            event.target.textContent = firstPick["icon"];
            event.target.classList.add(firstPick["class"])
            firstPick["element"].textContent = "";
        }
        firstPick = false;
        turn = false;
    }
});
