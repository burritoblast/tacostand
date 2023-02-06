import sys

def test_conversion_functions():
    assert inches_to_mm(1) == 25.4
    assert inches_to_cm(1) == 2.54
    assert inches_to_m(1) == 0.0254

def inches_to_mm(inches):
    return inches * 25.4

def inches_to_cm(inches):
    return inches * 2.54

def inches_to_m(inches):
    return inches * 0.0254

if '-t' in sys.argv:
    test_conversion_functions()