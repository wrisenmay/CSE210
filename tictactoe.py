board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
current_player = "X"
winner = None
game_running = True

def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])

def player_input(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = current_player
    else:
        print("That spot is already taken!")

def horizontal_check(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def row_check(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    if board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    if board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def diagonal_check(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def tie_check(board):
    global game_running
    if "-" not in board:
        print_board(board)
        print("It's a tie!")
        game_running = False

def win_check():
    global game_running
    if diagonal_check(board) or horizontal_check(board) or row_check(board):
        print_board(board)
        print(f"The winner is {winner}!")
        game_running = False


def player_switch():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def main():
    while game_running:
        print_board(board)
        player_input(board)
        win_check()
        tie_check(board)
        player_switch()

main()

