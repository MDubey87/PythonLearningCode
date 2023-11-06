def drawBoard(board):
    rows=len(board)
    cols=len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], "  |", board[r][1], " |", board[r][2])
        print("---+---+---")

def createBoard():
    return [["" for n in range(3)] for i in range(3)]

def symbol():
# This function decides the players' symbols
    symbol1 = input("Player 1, do you want to be X or O? ")
    if symbol1.upper() == "X":
        symbol2 = "O"
        print("Player 2, you are O. ")
    else:
        symbol2 = "X"
        print("Player 2, you are X. ")
    input("Press enter to continue.")
    print("\n")
    return (symbol1, symbol2)

def startGame(symbol1, symbol2, board):
    count=1
    winner=True
    while count <10 and winner== True:
        playGame(symbol1,symbol2,board,count)
        drawBoard(board)
        if count == 9:
            print("Board is full")
            if winner == True :
                print("Game is tie.")
        # check the winner
        winner= isWinner(board,symbol1,symbol2)
        count+=1
    if winner == False:
        print("Game over.")

# This function will pay the game
def playGame(symbol1, symbol2, board, count):
    # Decides the turn
    if count % 2 == 0:
        player = symbol1
    elif count % 2 == 1:
        player = symbol2
    print("Player "+ player + ", it is your turn. ")
    row = int(input("Pick a row:"
                    "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"))
    column = int(input("Pick a column:"
                       "[left column: enter 0, middle column: enter 1, right column enter 2]"))
    # Check if players' selection is out of range
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        print("Out of boarder. Pick another one. ")
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                           "[left column: enter 0, middle column: enter 1, right column enter 2]"))
     # Check if the square is already filled
    while (board[row][column] == symbol1)or (board[row][column] == symbol2):
        print("The square you picked is already filled. Pick another one.")
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                            "[left column: enter 0, middle column: enter 1, right column enter 2]"))  
    # Locates player's symbol on the board
    if player == symbol1:
        board[row][column] = symbol1
            
    else:
        board[row][column] = symbol2
    
    return board

# This function checks if any winner is winning
def isWinner(board, symbol1, symbol2):
    winner = True
    # Check the rows
    for row in range (0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol1):
            winner = False
            print("Player " + symbol1 + ", you won!")
   
        elif (board[row][0] == board[row][1] == board[row][2] == symbol2):
            winner = False
            print("Player " + symbol2 + ", you won!")
            
            
    # Check the columns
    for col in range (0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol1):
            winner = False
            print("Player " + symbol1 + ", you won!")
        elif (board[0][col] == board[1][col] == board[2][col] == symbol2):
            winner = False
            print("Player " + symbol2 + ", you won!")

    # Check the diagnoals
    if board[0][0] == board[1][1] == board[2][2] == symbol1:
        winner = False 
        print("Player " + symbol1 + ", you won!")

    elif board[0][0] == board[1][1] == board[2][2] == symbol2:
        winner = False
        print("Player " + symbol2 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol1:
        winner = False
        print("Player " + symbol1 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol2:
        winner = False
        print("Player " + symbol2 + ", you won!")
    return winner


def main():
    board = createBoard()
    drawBoard(board)
    symbol_1,symbol_2 = symbol()
    # Game will start
    startGame(symbol_1,symbol_2,board)

# Calling main method
main()
