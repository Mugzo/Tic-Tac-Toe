import numpy as np


class Game:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def show_board(self):
        print_board = ""
        for pos in range(len(self.board)):
            if self.board[pos] == 0:
                print_board += "_"
            elif self.board[pos] == 1:
                print_board += "X"
            elif self.board[pos] == 2:
                print_board += "O"
            if (pos + 1) % 3 == 0:
                print_board += "\n"
        print(print_board)

    def player(self, player, warning=False):
        print(f"Turn: Player {player}")
        self.show_board()
        if warning:
            print("This is an illegal move, please choose a legal move.")
        position = int(input("What position do you choose: "))
        if self.board[position - 1] != 0:
            self.player(player, warning=True)
        else:
            self.board[position - 1] = player

    def check_winner(self, player):
        array = np.array(self.board).reshape(-1, 3)
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
                print(f"Player {player} won the game!")
                self.show_board()
                return False
            # Verify if it's a draw
            elif 0 not in self.board:
                self.show_board()
                print("The game is a draw.")
                return False
        return True


def play():
    print("To choose your position please refer to this board, where the numbers are the position:")
    print("1 2 3\n"
          "4 5 6\n"
          "7 8 9\n")
    print("Player 1 starts.")

    game_is_on = True
    game = Game()

    while game_is_on:
        game.player(1)
        if not game.check_winner(1):
            game_is_on = False
            break
        game.player(2)
        if not game.check_winner(2):
            game_is_on = False
            break


play()