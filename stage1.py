#STAGE 1
# stage1.py script will print the tic-tac-toe game board and script will be called from the other scripts

# Create list of 3 lists
board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

# Create board function
def print_board():
    print("Printing board...")
    for i in range(len(board)):
        print(board[i])

# unit test
#print_board()