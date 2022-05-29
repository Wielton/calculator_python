class CalculatorInputError(ValueError):
    def __init__(self):
        ValueError.__init__(self)
        
class FunctionSelectionError(Exception):
    def __init__(self):
        Exception.__init__(self, "Please Choose between 1 and 4: ")