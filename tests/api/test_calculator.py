from utils.calculator import add
from utils.calculator import subtract

def test_add():
    assert(add(2, 3)) == 5

def test_subtract():
    assert(subtract(1, 1)) == 0


