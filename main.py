from flask import Flask, render_template, jsonify
from game import Game

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/game/<positions>", methods=["POST", "GET"])
def game(positions):
    board = [int(x) for x in positions.split(",")]
    game = Game(board)

    player = game.is_winner(board)

    # If the game is not ended continue, else pass the game state to Javascript (Win or draw)
    if player is False:
        pass
    elif player == -1:
        return jsonify(True)
    elif player == 0:
        return jsonify(None)

    move = game.minimax(game.board, 6, True)[1]
    index = game.get_index(move)
    ai = game.is_winner(move)

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

# To do
# Add Alpha Beta Pruning to the Minimax algorithm
# Add a database to track the AI stats
# Make the AI take random moves from its best possibilities so the game looks a bit different each time.
# Host the game online
