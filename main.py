from flask import Flask, render_template, jsonify, request
from game import Game

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/game/<positions>", methods=["POST", "GET"])
def game(positions):
    board = [int(x) for x in positions.split(",")]
    game = Game(board)

    winner = game.is_winner()
    return jsonify(winner)


if __name__ == "__main__":
    app.run(debug=True)
