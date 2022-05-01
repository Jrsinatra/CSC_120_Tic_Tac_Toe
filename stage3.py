# Import user defined functions
import stage1

# Function to check for win
def check_win(playerId):
    win = False
    # Check rows and columns for win
    for i in range(len(stage1.board)):
        # Check for 3 in a row horizontally
        if (stage1.board[i][0] != "-") and (stage1.board[i][0] == stage1.board[i][1]) and (stage1.board[i][1] == stage1.board[i][2]):
            win = True
        # Check for 3 in a row vertically
        elif (stage1.board[0][i] != "-") and (stage1.board[0][i] == stage1.board[1][i]) and (stage1.board[1][i] == stage1.board[2][i]):
            win = True
    # Check diagonals for win
    if stage1.board[0][0] != "-" and stage1.board[0][0] == stage1.board[1][1] and stage1.board[1][1] == stage1.board[2][2]:
        win = True
    elif stage1.board[0][2] != "-" and stage1.board[0][2] == stage1.board[1][1] and stage1.board[1][1] == stage1.board[2][0]:
        win = True
    return win

