#Test the Tick Tack Toe Game using pytest

from tick_tack import *
import pytest
import sys
from io import StringIO

# Test Check Board Size Function
def test_check_board_size():
    # Test that the board size is valid
    assert checkBoardSize(3, 3) == True
    # Test that the board size is invalid
    assert checkBoardSize(3, 2) == False

def test_check_symbols():
    # Test that the symbols are valid
    assert checkSymbols("X", "O") == True
    # Test that the symbols are invalid
    assert checkSymbols("X", "X") == False

#Test Player 1 Win Situation
def test_player1_win():
    #Create a new instance of the draw board class
    board = db.DrawBoard(3, 3, "Player 1", "Player 2", "X", "O")
    sys.stdin = StringIO("0,0 \n 0,1 \n 1,0 \n 1,1 \n 2,0")
    board.getMoves()
    assert board.player1Win == True


#Test Player 2 Win Situation
def test_player2_win():
    #Create a new instance of the draw board class
    board = db.DrawBoard(3, 3, "Player 1", "Player 2", "X", "O")
    sys.stdin = StringIO("2,2 \n 0,0 \n 1,0 \n 0,1 \n 2,0 \n 0,2")
    board.getMoves()
    assert board.player2Win == True


#Run the Main Test
pytest.main(["-v", "--tb=line", "-rN", __file__])
