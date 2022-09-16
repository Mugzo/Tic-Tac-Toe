const squares = document.querySelectorAll(".square")
const playAgain = document.getElementById("restart")

let positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]

let startingPlayer = "x"
let turnPlayer = "x"

let winner

activateGameListener()

playAgain.addEventListener("click", restartBoard)


function activateGameListener() {
    squares.forEach(square => {
        square.addEventListener('click', handleClick, { once: true })
    })
}


function deactivateGameListener() {
    squares.forEach(square => {
        square.removeEventListener("click", handleClick)
    })
}


function handleClick(e) {
    const square = e.target
    const squareID = e.target.id

    if (square.lastElementChild.classList.length === 0){
        square.lastElementChild.classList.add(turnPlayer)

        turnPlayer === "x" ? positions[squareID- 1] = 1 : positions[squareID - 1] = 2
        turnPlayer === "x" ? turnPlayer = "o" : turnPlayer = "x"

        deactivateGameListener()

        requestServer()
    }
}

function requestServer(){
    fetch(`/game/${positions}`)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            if (data === true) {
                game_win()
            }
            else if (data === null) {
                game_draw()
            }
            else if (data[0] === false) {
                squares[data[1]].lastElementChild.classList.add(turnPlayer)
                positions[data[1]] = 2
                turnPlayer === "x" ? turnPlayer = "o" : turnPlayer = "x"
                if (data[2] === true) {
                    game_win()
                }
                else if (data[2] === null) {
                    game_draw()
                }
                else {
                    activateGameListener()
                }
            }
        })
}

function restartBoard() {
    positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    document.getElementById("restart").classList.add("hidden")
    document.getElementById("game-result").innerHTML = ""

    squares.forEach(square => {
        if (square.lastElementChild.classList.length === 1) {
            square.lastElementChild.removeAttribute("class")
        }
    })

    turnPlayer = startingPlayer
    activateGameListener()

    if (turnPlayer === "o") {
        deactivateGameListener()
        requestServer()
    }
}

function game_win() {
    deactivateGameListener()
    turnPlayer === "o" ? winner = "Player" : winner = "AI"
    document.getElementById("game-result").innerHTML = `${winner} wins!`
    startingPlayer === "x" ? startingPlayer = "o" : startingPlayer = "x"
    playAgain.classList.remove("hidden")
}

function game_draw() {
    document.getElementById("game-result").innerHTML = "It's a draw!"
    startingPlayer === "x" ? startingPlayer = "o" : startingPlayer = "x"
    playAgain.classList.remove("hidden")
}