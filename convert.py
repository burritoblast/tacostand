import sys

def inches_to_mm(inches):
    return inches * 25.4

def inches_to_cm(inches):
    return inches * 2.54

def inches_to_m(inches):
    return inches * 0.0254

def test_conversions():
    assert inches_to_mm(1) == 25.4
    assert inches_to_cm(1) == 2.54
    assert inches_to_m(1) == 0.0254
    assert inches_to_mm(2.5) == 63.5
    assert inches_to_cm(5.5) == 13.97
    assert inches_to_m(10) == 0.254

if __name__ == '__main__':
    if '-t' in sys.argv:
        test_conversions()
    else:
        value = float(input("Enter the value to be converted from inches: "))
        unit = input("What unit of measurement would you like to convert it to? (mm, cm, m): ")
        if unit == 'mm':
            print(f"{value} inches is {inches_to_mm(value)} millimeters")
        elif unit == 'cm':
            print(f"{value} inches is {inches_to_cm(value)} centimeters")
        elif unit == 'm':
            print(f"{value} inches is {inches_to_m(value)} meters")
        else:
            print("Invalid unit specified. Please try again.")
