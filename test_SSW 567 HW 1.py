from SSW_567_HW_1 import classify_triangle

def test_equilateral_triangle():
    assert classify_triangle(2,2,2) == 'equilateral'

def test_right_triangle():
    assert classify_triangle(3,4,5) == 'right'
    assert classify_triangle(10,6,8)

def test_scalene_triangle():
    assert classify_triangle(2,3,4) == 'scalene'
    assert classify_triangle(4,3,2) == 'scalene'

def test_isocoles_triangle():
    assert classify_triangle(2,2,4) == 'iscocoles'
    assert classify_triangle(10,10,5) == 'iscocoles'

