import numpy as np
from copy import deepcopy
import random


class Game:
    def __init__(self, position):
        self.board = position

    def is_winner(self, position):
        array = np.array(position).reshape(-1, 3)
        # Winning lines
        lines = []
        # Verticals and Horizontals
        for a in range(3):
            lines.append(array[:, a])
            lines.append(array[a])

        # Diagonals
        lines.append(array.diagonal())
        lines.append(np.fliplr(array).diagonal())

        # Verify if there is a winner
        for line in lines:
            if not np.any(line == 0) and np.sum(line) % 3 == 0:
                if np.sum(line) == 3:
                    return -1
                else:
                    return 1
        # Verify if it's a draw
        if 0 not in position:
            return 0
        return False

    def get_all_moves(self, position, turn):
        moves = []
        # Find all possible moves
        for pos in range(len(position)):
            temp_position = deepcopy(position)
            if temp_position[pos] == 0:
                if turn == "player":
                    temp_position[pos] = 1
                else:
                    temp_position[pos] = 2
                moves.append(temp_position)

        return moves

    def minimax(self, position, depth, maximizing_player):
        if depth == 0 or self.is_winner(position) is not False:
            if self.is_winner(position) is False:
                score = 0
            else:
                score = self.is_winner(position)
            return score, position

        if maximizing_player:
            maxEval = float("-inf")
            best_move = None
            for move in self.get_all_moves(position, "ai"):
                evaluation = self.minimax(move, depth - 1, False)[0]
                maxEval = max(maxEval, evaluation)
                print(f"turn: ai, position: {move}, evaluation: {maxEval}")
                if maxEval == evaluation:
                    best_move = move
            return maxEval, best_move

        else:
            minEval = float("inf")
            best_move = None
            for move in self.get_all_moves(position, "player"):
                evaluation = self.minimax(move, depth - 1, True)[0]
                minEval = min(minEval, evaluation)
                print(f"turn: Player, position: {move}, evaluation: {minEval}")
                if minEval == evaluation:
                    best_move = move
            return minEval, best_move

    # Get the index of the AI move to pass it to the Javascript
    def get_index(self, new_position):
        original_position = np.array(self.board)
        new_position = np.array(new_position)

        move = new_position - original_position

        index = np.where(move == 2)[0].tolist()[0]

        return index

