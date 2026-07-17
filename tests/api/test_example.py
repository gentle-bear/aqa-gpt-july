def test_project_is_configured():
    assert 2 + 2 == 4, 'Результат сложения неверный'
    
    
def test_subtraction():
    assert 10 - 4 == 6, 'Результат вычитания неверный'
    
def test_multiplication():
    assert 4 * 5 == 20, 'Результат умножения неверный'
    
def test_division():
    assert 20 / 5 == 4, 'Результат деления неверный'

def test_string():
    assert 'string' != 'String'