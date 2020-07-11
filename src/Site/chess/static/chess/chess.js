// alert(pieces)

function addFirstPlayerPieces() {
    piece_row = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1']
    pieces = ['\u2656', '\u2658', '\u2657', '\u2655', '\u2654', '\u2657','\u2658', '\u2656']
    piece_row.forEach((element, index)=>{
        piece = document.querySelector(`#${element}`)
        piece.classList.add("player-one-pieces")
        piece.textContent=`${pieces[index]}`
    })

    pawns_row = ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2']
    pawns_row.forEach(element => {
       pawn = document.querySelector(`#${element}`)
        pawn.classList.add("player-one-pieces")
        pawn.textContent = '\u2659'; 
    });
}
function addSecondPlayerPieces() {
    piece_row = ['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8']
    pieces = ['\u265C', '\u265E', '\u265D', '\u265B', '\u265A', '\u265D','\u265E', '\u265C']
    piece_row.forEach((element, index)=>{
        piece = document.querySelector(`#${element}`)
        piece.classList.add("player-two-pieces")
        piece.textContent=`${pieces[index]}`
    })

    pawns_row = ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7']
    pawns_row.forEach(element => {
       pawn = document.querySelector(`#${element}`)
        pawn.classList.add("player-two-pieces")
        pawn.textContent = '\u265F'; 
    });
}
addFirstPlayerPieces();
addSecondPlayerPieces()
