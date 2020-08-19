import { Piece, Rook, Knight, Bishop, Queen, King, Pawn } from "./piece.js"

pieces.forEach(element => {
    let boardSquare = document.querySelector(`#${element.square}`)
    if(element.id !== "None"){
        boardSquare.children[0].setAttribute("id", `piece-${element.id}`)
        boardSquare.children[0].textContent=`${element.icon}`;
    }
});
p1Pieces.forEach(element=>{
    let p1piece = document.querySelector(`#piece-${element.id}`);
    if(p1piece){
        p1piece.classList.add("player-one-pieces");
    }
})

p2Pieces.forEach(element=>{
    let p2piece = document.querySelector(`#piece-${element.id}`);
    if(p2piece) {
        p2piece.classList.add("player-two-pieces");
    }
})

let endpoint = window.location.protocol == 'https:' ? 'wss://' : 'ws://' + window.location.host + window.location.pathname
let socket = new WebSocket(endpoint);
socket.onopen= function(e){
    console.log("open", e)
}

socket.onmessage = function(e){
    console.log("message", e);
    let piece = JSON.parse(e.data)
    let firstPiece = piece.message.firstPiece
    let secondPiece = piece.message.secondPiece
    let firstSquare = document.querySelector(`#${piece.message.firstPiece.square}`)
    let secondSquare = document.querySelector(`#${piece.message.secondPiece.square}`)
    secondSquare.innerHTML = `<span id=${firstPiece.id}>${firstPiece.piece}</span>`
    firstSquare.children[0].removeAttribute("id")
    firstSquare.children[0].textContent=""
    secondSquare.children[0].classList = firstSquare.children[0].classList
    firstSquare.children[0].classList.remove(firstSquare.children[0].classList[0])
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
            console.log(event.target)
            let id;
            let square;
            if( event.target.nodeName == "TD"){
                id = event.target.children[0].getAttribute("id")
                square = event.target.getAttribute("id")
            }
            else if ( event.target.nodeName == "SPAN") {
                id = event.target.getAttribute("id")
                square = event.target.parentElement.getAttribute("id")
            }
            selectedFirstPiece = {
                'piece': event.target.textContent,
                'square': square,
                "id": id
            }
        }
    }

    else if(event.target.closest('td') && firstClick ){
        console.log("Second Selected")
        firstClick = false;
        let id;
            if( event.target.nodeName == "TD"){
                id = event.target.children[0].getAttribute("id")
            }
            else if ( event.target.nodeName == "SPAN") {
                id = event.target.getAttribute("id")
            }
        selectedSecondPiece =  {
            'piece': event.target.textContent,
            'square': event.target.getAttribute("id"),
            "id": id
        }
        socket.send(JSON.stringify({'firstPiece': selectedFirstPiece, 'secondPiece': selectedSecondPiece}))
    }
});


socket.onerror= function(e){
    console.log("error", e)
}

socket.onclose= function(e){
    console.log("close", e)
}
