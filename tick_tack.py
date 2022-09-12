#Import the draw board file and use the class to draw the board
import gamefiles.draw_board as db


def main() :
    #Get Player 1's name
    player1 = input("Player 1, enter your name: ")
    #Get Player 1's symbol
    symbol1 = input("Player 1, enter your symbol: ")
    #Get Player 2's name
    player2 = input("Player 2, enter your name: ")
    #Get Player 2's symbol
    symbol2 = input("Player 2, enter your symbol: ")
    #Check if the symbols are the same
    while checkSymbols(symbol1,symbol2) == False :
        print("Symbols Must Be Different")
        symbol2 = input("Player 2, enter your symbol: ")
    #Get the width of the board
    width = GetInt("Enter the width of the board: ")
    #Get the height of the board
    height = GetInt("Enter the height of the board: ")
    #Board must be at least 3x3
    while checkBoardSize(width,height) == False :
        print("Board Must Be At Least 3x3")
        width = GetInt("Enter the width of the board: ")
        height = GetInt("Enter the height of the board: ")
        #Create a new instance of the draw board class
    board = db.DrawBoard(width, height, player1, player2, symbol1, symbol2)
    #Get the players moves    
    board.getMoves()


def GetInt(prompt) :
    while True :
        try :
            value = int(input(prompt))
            return value
        except ValueError :
            print("Invalid Value Entered. Value Must Be A Whole Number")

def checkSymbols(symbol1,symbol2) :
    if symbol1 == symbol2 :
        return False
    return True
        
def checkBoardSize(width,height) :
    if width < 3 or height < 3 :
        return False
    return True

if __name__ == "__main__" :
    main()
