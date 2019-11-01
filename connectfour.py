from disappear import delete_lines, delete_line, disappearing_input

class ConnectFour:
    def __init__(self, width: int = 7, height: int = 6):
        self.width = width
        self.height = height
        self.board = [
            [' ' for j in range(height)] for i in range(width)
        ]
        self.isP1Turn = True
        self.p1Char = 'X'
        self.p2Char = 'O'
        # # colours!
        # self.p1Char = '\u001b[31m█\u001b[0m'
        # self.p2Char = '\u001b[33m█\u001b[0m'
        # # 'bright' colours
        # self.p1Char = '\u001b[31;1m█\u001b[0m'
        # self.p2Char = '\u001b[33;1m█\u001b[0m'
        
        self.winner = None

    def board_str(self):
        out = ''

        # add the top of the board to output
        head = '┌' + '───┬' * (self.width - 1) + '───┐' + '\n'
        out += head

        # add board values to output
        for i in range(self.height):
            line = '│'
            for j in range(self.width):
                line += self.board[j][i].ljust(2, ' ').rjust(3, ' ') + '│'
            out += line + '\n'
            # if the row is not the last, add a separator to output
            if (i != self.height - 1):
                separator = '├' + '───┼' * (self.width - 1) + '───┤' + '\n'
                out += separator
            # otherwise add the end of the board to output
            else:
                end = '└' + '───┴' * (self.width - 1) + '───┘' + '\n'
                out += end

        # add column numbers to output
        for i in range(self.width):
            if (self.is_valid_move(i)):
                out += ' ' + str(i).ljust(2, ' ').rjust(3, ' ')
            else:
                out += '    '

        return out + '\n'

    def show(self):
        print(self.board_str())

    def unshow(self):
        delete_lines(self.board_str())

    def is_valid_move(self, column: int):
        col_list = [self.board[column][i] for i in range(self.height)]
        return any(cell == ' ' for cell in col_list)

    def check_winner(self):
        is_winning_move = False
        board = self.board

        # Check horizontal win
        for c in range(self.width - 3):
            for r in range(self.height):
                if board[c][r] == board[c+1][r] == board[c+2][r] == board[c+3][r] != ' ':
                    is_winning_move = True

        # Check vertical win
        for c in range(self.width):
            for r in range(self.height-3):
                if board[c][r] == board[c][r+1] == board[c][r+2] == board[c][r+3] != ' ':
                    is_winning_move = True

        # Check upward diagonal win
        for c in range(self.width - 3):
            for r in range(self.height-3):
                if board[c][r] == board[c-1][r+1] == board[c-2][r+2] == board[c-3][r+3] != ' ':
                    is_winning_move = True

        # Check downward diagonal win
        for c in range(self.width - 3):
            for r in range(self.height-3):
                if board[c][r] == board[c+1][r+1] == board[c+2][r+2] == board[c+3][r+3] != ' ':
                    is_winning_move = True

        if is_winning_move:
            self.winner = 2 if self.isP1Turn else 1

    def get_valid_columns(self):
        valid_columns = []
        for i in range(self.width):
            if self.board[i].count(' '):
                valid_columns.append(i)
        return valid_columns

    def get_current_char(self):
        return self.p1Char if self.isP1Turn else self.p2Char

    def insert(self, column: int):
        for i in reversed(range(self.height)):
            if self.board[column][i] == ' ':
                self.board[column][i] = self.get_current_char()
                self.check_winner()
                break

        self.isP1Turn = not self.isP1Turn

    def is_board_full(self):
        return all(all(cell != ' ' for cell in row) for row in self.board)

    def get_player_turn(self):
        selection_is_valid = False
        player_selection_text = f"Player {f'1 [{self.p1Char}' if self.isP1Turn else f'2 [{self.p2Char}'}] pick an open cell: "
        error_text = 'Only input a number shown above. Press ENTER to try again. '
        selection = 0

        def show_error_message():
            temp = input(error_text)
            delete_line(error_text + temp)

        while not selection_is_valid:
            selection = disappearing_input(player_selection_text + ' \b')
            try:
                selection = int(selection)
                if selection in self.get_valid_columns():
                    selection_is_valid = True
                else:
                    show_error_message()
            except Exception:
                show_error_message()

        return selection

    def play(self):
      # self.winner == None and 
        while not self.is_board_full():
            self.show()
            move = self.get_player_turn()
            self.insert(move)
            self.check_winner()

            self.unshow()

        if not self.winner:
            print("Both of you suck! Get a life!")
        else:
            winner = self.winner
            loser = 1 if winner == 2 else 2
            print(f"Player {winner} wins! Player {loser} sucks!")

    def __str__(self):
        return self.board_str()


def main():
    play = True
    while play:
        board = ConnectFour()
        board.play()

        play_again = disappearing_input("Play again? (y/n)")
        if play_again.lower() not in ['y', 'yes']:
            play = False


if __name__ == '__main__':
    main()
    file.close()
