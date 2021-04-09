"use strict";
/**
 * Exercise #4: Countdown timer
 */

let timeLeft = -1
let timer = null;

function init(){

    document.querySelector("form[name='countdown_form']").onsubmit = 
        function(event) {
            event.preventDefault();  // preventing the form from submission

            // set time left (seconds)
            timeLeft = this.querySelector("#minutes").value * 60;

            this.style.display = "none";  // hide form
            document.querySelector("#countdown").style.display = "block";  // show countdown div
            timer = setInterval(ontick,1000);
            setDisplay(true)
            
    }

}

function ontick(){
    timeLeft--;
    setDisplay(false)
    if (timeLeft === 0){
        alert("Time is up!")
        document.getElementById("countdown").style.display = "none"
        document.querySelector("form[name='countdown_form']").style.display = "block"
        clearInterval(timer)
    }
}

function setDisplay(isInitial){
    document.getElementById("timer").innerHTML = getSecondDisplay(timeLeft)
    
    let progress = document.getElementById("progressbar");
    console.log(progress)
    if (isInitial){
        progress.max = timeLeft;
    }
    progress.value = timeLeft;
}

function getSecondDisplay(seconds){
    const min = Math.floor(seconds/60);
    seconds = seconds % 60;
    let str = (min < 10) ? "0": "";
    str += min + ":";
    str += (seconds <10) ? "0" + seconds: seconds;
    return str;
}

window.onload = init;