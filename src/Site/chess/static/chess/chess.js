import { Piece, Rook, Knight, Bishop, Queen, King, Pawn } from "./piece.js"

pieces.forEach(element => {
    let boardSquare = document.querySelector(`#${element.square}`)
    boardSquare.innerHTML=`<span id=${element.id}>${element.icon}</span>`;
});

let endpoint = window.location.protocol == 'https:' ? 'wss://' : 'ws://' + window.location.host + window.location.pathname
let socket = new WebSocket(endpoint);
socket.onopen= function(e){
    console.log("open", e)
}

socket.onmessage = function(e){
    console.log("message", e);
    let piece = JSON.parse(e.data)
    let firstSquare = document.querySelector(`#${piece.message.firstPiece.square}`)
    let secondSquare = document.querySelector(`#${piece.message.secondPiece.square}`)
    secondSquare.textContent = firstSquare.textContent
    firstSquare.textContent = ""
    console.log(piece)
    console.log(firstSquare);

}

let table = document.querySelector("table")
let firstClick = false;
let selectedFirstPiece;
let selectedSecondPiece;
table.addEventListener("click", function(event){

    if(event.target.closest('td') && !firstClick ){
        console.log("First Selected")
        if (event.target.textContent){
            firstClick = true;

            selectedFirstPiece = {'piece': event.target.textContent,
            'square': event.target.getAttribute("id"),
            "id": event.target.children[0].getAttribute("id")}
        }
    }
    else if(event.target.closest('td') && firstClick ){
        console.log("Second Selected")
        firstClick = false;
        selectedSecondPiece =  {'piece': event.target.textContent,
        'square': event.target.getAttribute("id"),
        "id": event.target.children[0].getAttribute("id")}
        socket.send(JSON.stringify({'firstPiece': selectedFirstPiece, 'secondPiece': selectedSecondPiece}))
    }
   
});


socket.onerror= function(e){
    console.log("error", e)
}

socket.onclose= function(e){
    console.log("close", e)
}

// addFirstPlayerPieces();
// addSecondPlayerPieces()

// let table = document.querySelector("table")
// let firstPick = false;
// let secondPick;
// let turn = false;

// table.addEventListener("click", function(e){
//     console.log("CLICKED");

//     if(event.target.matches('td') && !turn && !firstPick && event.target.textContent.length){
//        let all_classes = event.target.classList
//        let player_class = all_classes[1]
//         firstPick = {"icon" : event.target.textContent,
//                     "class": player_class,
//                     "element": event.target}
//         turn = true;
//     }
//     else if (event.target.matches('td') && turn && firstPick ) { 
//         if(event.target.textContent !== firstPick["element"].textContent){
//             let all_classes = event.target.classList
//             if( all_classes.length > 1 ){
//                 event.target.classList.remove(all_classes[1])
//             }
//             event.target.textContent = firstPick["icon"];
//             event.target.classList.add(firstPick["class"])
//             firstPick["element"].textContent = "";
//         }
//         firstPick = false;
//         turn = false;
//     }
// });

// export {table};