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

    square.lastElementChild.classList.add(turnPlayer)

    turnPlayer === "x" ? positions[squareID- 1] = 1 : positions[squareID - 1] = 2

    fetch(`/game/${positions}`)
        .then(response => response.json())
        .then(data => {
            if (data === true) {
                deactivateGameListener()
                turnPlayer === "x" ? winner = "Player" : winner = "AI"
                document.getElementById("game-result").innerHTML = `${winner} wins!`
                startingPlayer === "x" ? startingPlayer = "o" : startingPlayer = "x"
                playAgain.classList.remove("hidden")
            }
            else if (data === false) {
                turnPlayer === "x" ? turnPlayer = "o" : turnPlayer = "x"
            }
            else if (data === null) {
                document.getElementById("game-result").innerHTML = "It's a draw!"
                startingPlayer === "x" ? startingPlayer = "o" : startingPlayer = "x"
                playAgain.classList.remove("hidden")
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
}
