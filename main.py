from flask import Flask, render_template, jsonify
from game import Game
import time
import random

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/game/<positions>", methods=["POST", "GET"])
def game(positions):
    board = [int(x) for x in positions.split(",")]
    game = Game(board)

    # If AI is first to play, make a random move
    if 1 not in board:
        return jsonify(False, random.randint(0, 8), False)

    player = game.is_winner(board)

    # If the game is not ended continue, else pass the game state to Javascript (Win or draw)
    if player is False:
        pass
    elif player == -1:
        return jsonify(True)
    elif player == 0:
        return jsonify(None)

    start_time = time.time()
    move = game.minimax(game.board, 6, True)
    end_time = time.time()

    # Calculate the AI Evaluation time
    print(f"Evaluation Time: {end_time - start_time:.2f}")

    print(f"AI Move: {move[1]}, Evaluation: {move[0]}")
    index = game.get_index(move[1])
    ai = game.is_winner(move[1])

    # If the AI move doesn't result in the end of the game continue, else pass the game state to Javascript (Win or draw)
    if ai is False:
        ai = False
    elif ai == 1:
        ai = True
    elif ai == 0:
        ai = None

    # Returns if the player won, if not it returns the AI move and the game state after the AI move.
    return jsonify(player, index, ai)


if __name__ == "__main__":
    app.run(debug=True)
