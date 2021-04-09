"use strict";
/**
 * Exercise #5: Card board
 */


function init(){

    let form = document.querySelector("form[name='layout_form']");
    form.onsubmit = layout;
    
}
function turn(){
    this.style.transform= "rotateY(180deg)";
}

function layout(event){
    event.preventDefault();

    let layout = document.querySelector("#layout").value.split("x");
    let board = document.querySelector("#cardboard");

    board.innerHTML = ""

    for (let i = 0; i < layout[0] * layout[1]; i++){
        let card = document.createElement("div");
        card.classList.add("card");
        board.appendChild(card);
        card.addEventListener("click",turn)
    }

    board.style.width = 114 * layout[0] + 'px'
}
window.onload = init;