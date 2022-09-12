#Test the Tick Tack Toe Game using pytest

from tick_tack import *
import pytest

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

#Run the Main Test
pytest.main(["-v", "--tb=line", "-rN", __file__])
