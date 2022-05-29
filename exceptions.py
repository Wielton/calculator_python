class CalculatorInputError(Exception):
    def __init__(self,value):
        message = f'{value} is not a number. Choose again...'
        super().__init__(message)
        
class FunctionSelectionError(Exception):
    def __init__(self, value):
        message = f'{value} is not an available selection. Choose again...'
        super().__init__(message)