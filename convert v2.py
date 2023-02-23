class UnitConverter:
    def __init__(self):
        self.conversions = {
            'feet': {'inches': 12.0, 'meters': 0.3048},
            'inches': {'feet': 1/12.0, 'millimeters': 25.4, 'centimeters': 2.54, 'meters': 0.0254},
            'millimeters': {'inches': 1/25.4, 'centimeters': 0.1, 'meters': 0.001},
            'centimeters': {'inches': 1/2.54, 'millimeters': 10, 'meters': 0.01},
            'meters': {'feet': 3.28084, 'inches': 39.3701, 'millimeters': 1000, 'centimeters': 100},
            'pints': {'quarts': 0.5, 'cups': 2, 'milliliters': 473.176, 'deciliters': 47.3176, 'liters': 0.473176},
            'quarts': {'pints': 2, 'cups': 4, 'milliliters': 946.353, 'deciliters': 94.6353, 'liters': 0.946353},
            'cups': {'pints': 0.5, 'quarts': 0.25, 'milliliters': 236.588, 'deciliters': 23.6588, 'liters': 0.236588},
            'milliliters': {'pints': 0.00211338, 'quarts': 0.00105669, 'cups': 0.00422675, 'deciliters': 0.1, 'liters': 0.001},
            'deciliters': {'pints': 0.0441829, 'quarts': 0.0220915, 'cups': 0.0883662, 'milliliters': 10, 'liters': 0.1},
            'liters': {'pints': 2.11338, 'quarts': 1.05669, 'cups': 4.22675, 'milliliters': 1000, 'deciliters': 10}
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversions or to_unit not in self.conversions[from_unit]:
            return None
        return value * self.conversions[from_unit][to_unit]

if __name__ == '__main__':
    converter = UnitConverter()

    value = float(input("Enter value to convert: "))
    
    from_unit = input("Enter unit to convert from: ")
    to_unit = input("Enter unit to convert to: ")

    result = converter.convert(value, from_unit, to_unit)

    if result is not None:
        print(f"{value} {from_unit} = {result} {to_unit}")
    else:
        print("Invalid conversion")
