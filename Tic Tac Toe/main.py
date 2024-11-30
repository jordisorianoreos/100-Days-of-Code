import numpy as np

board = np.array([[" ", " ", " "],
                  [" ", " ", " "],
                  [" ", " ", " "]])

X_O = ['X', 'O']
is_game_over = False


def valid_input(input_coords):
    input_coords = [x.strip() for x in input_coords.replace(" ", "").split(".")]

    if len(input_coords) == 2 and all(x.isdigit() for x in input_coords):
        input_coords = [int(x) - 1 for x in input_coords]
        x, y = input_coords
        if 0 <= x <= 2 and 0 <= y <= 2:
            return [x, y]
        else:
            print('error: Please enter valid coordinates.')
            return False
    else:
        print('error: Please enter valid coordinates.')
        return False


def check_board(board):
    global is_game_over
    X_O = ['X', 'O']

    for player_piece in X_O:

        # Checks the rows
        for row in range(3):
            if all(row_element == player_piece for row_element in board[row, :]):
                print(f"🎉 Player '{player_piece}' wins!")
                is_game_over = True

        # Checks the columns
        for column in range(3):
            if all(row_element == player_piece for row_element in board[:, column]):
                print(f"🎉 Player '{player_piece}' wins!")
                is_game_over = True

        # Descending diagonal
        if all(x == player_piece for x in board.diagonal()):
            print(f"🎉 Player '{player_piece}' wins!")
            is_game_over = True

        # Ascending diagonal
        if all(x == player_piece for x in np.flipud(board).diagonal()):
            print(f"🎉 Player '{player_piece}' wins!")
            is_game_over = True

    # Draw
    if np.all(board != ' '):
        print("🤝🏼 It's a draw!")
        is_game_over = True


def can_put_piece(coords, board):
    if coords and board[int(coords[0]), int(coords[1])] == ' ':
        return True
    else:
        print('error: There is a piece on that place.')
        return False


def print_board(board):
    board = board.tolist()

    for i in range(len(board)):
        if i == 1:
            print("-" * 11)
            print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ")
            print("-" * 11)
        else:
            print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ")


print("❌TIC TAC TOE⭕", "\n")
while not is_game_over:
    for player_symbol in X_O:
        print_board(board)
        print("\n")
        print(f"[ PLAYER {player_symbol}'s TURN ]")

        input_coords = input(">> Enter coordinates (e.g.: 1.3): ")
        coords = valid_input(input_coords)

        while not coords or not can_put_piece(coords, board):
            input_coords = input(">> Enter coordinates (e.g.: 1.3): ")
            coords = valid_input(input_coords)

        board[coords[0], coords[1]] = player_symbol

        check_board(board)

        if is_game_over:
            print_board(board)
            break
