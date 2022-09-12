class DrawBoard : 
    def __init__(self, width, height, player1, player2, symbol1, symbol2) :
        self.width = width
        self.height = height
        self.player1 = player1
        self.player2 = player2
        self.symbol1 = symbol1
        self.symbol2 = symbol2
        self.board = []
        #Create a board with the width and height
        for i in range(self.height) :
            self.board.append([])
            for j in range(self.width) :
                self.board[i].append(" ")
        #Set the players moves
        self.moves = []
        for i in range(self.height) :
            self.moves.append([])
            for j in range(self.width) :
                self.moves[i].append(False)
        self.moveCount = 0
        self.move = 0
        self.move1 = 0
        self.move2 = 0
        self.player1Win = False
        self.player2Win = False
        self.draw = False
    #Draw the board
    def drawBoard(self) :
        print("  ", end="")
        for i in range(self.width) :
            print(" ", i, end="")
        print()
        for i in range(self.height) :
            print(i, end=" ")
            for j in range(self.width) :
                print("|", self.board[i][j], end="")
            print("|")
    #Get the players moves
    def getMoves(self) :
        while self.player1Win == False and self.player2Win == False and self.draw == False :
            self.drawBoard()
            self.moveCount += 1
            if self.moveCount % 2 == 1 :
                self.move = self.move1
                self.player = self.player1
                self.symbol = self.symbol1
                self.move1 += 1
            else :
                self.move = self.move2
                self.player = self.player2
                self.symbol = self.symbol2
                self.move2 += 1
            self.move = input(self.player + ", enter your move (X,Y): ")
            self.move = self.move.split(",")
            try :
                self.move[0] = int(self.move[0])
                self.move[1] = int(self.move[1])
            except ValueError :
                print("Invalid Value Entered ") 
                self.moveCount -= 1
                continue
        #try to check if player move is in range
            if self.move[0] < 0 or self.move[0] >= self.width or self.move[1] < 0 or self.move[1] >= self.height :
                print("Move out of range")
                self.moveCount -= 1
            elif self.moves[self.move[0]][self.move[1]] == False :
                self.board[self.move[0]][self.move[1]] = self.symbol
                self.moves
                self.moves[self.move[0]][self.move[1]] = True
            else :
                print("That space is taken")
                self.moveCount -= 1
            self.checkWin()


#Check if the player has won by having filled a row or column or diagonal
    def checkWin(self) :
        #Check if the player has filled a row
        for i in range(self.height) :
            self.count = 0
            for j in range(self.width) :
                if self.board[i][j] == self.symbol :
                    self.count += 1
            if self.count == self.width :
                self.playerWin()
                return True
        #Check if the player has filled a column
        for i in range(self.width) :
            self.count = 0
            for j in range(self.height) :
                if self.board[j][i] == self.symbol :
                    self.count += 1
            if self.count == self.height :
                self.playerWin()
                return True
        #Check if the player has filled the right diagonal
        self.count = 0
        for i in range(self.height) :
            if self.board[i][i] == self.symbol :
                self.count += 1
        if self.count == self.height :
            self.playerWin()
            return True
        #Check if the player has filled the left diagonal
        self.count = 0
        for i in range(self.height) :
            if self.board[i][self.height - i - 1] == self.symbol :
                self.count += 1
        if self.count == self.height :
            self.playerWin()
            return True
        #Check if the game has ended in a draw
        if self.moveCount == self.width * self.height :
            self.draw = True
            print("Draw")
            return False


    #If the player has won
    def playerWin(self) :
        if self.symbol == self.symbol1 :
            self.player1Win = True
            print(self.player1 + " Wins")
        else :
            self.player2Win = True
            print(self.player2 + " Wins")