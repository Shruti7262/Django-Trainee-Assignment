# Description: You are tasked with creating a Rectangle class with the following requirements:

# An instance of the Rectangle class requires length:int and width:int to be initialized.
# We can iterate over an instance of the Rectangle class 
# When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

# CODE:
class Rectangle:
    def __init__(self, length: int, width: int):
        if not isinstance(length, int) or not isinstance(width, int): # check TypeError 
            raise TypeError("Length and width must be integers.")
        if length <= 0 or width <= 0:                                 # check ValueError
            raise ValueError("Length and width must be positive.")
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}  # using yield to return the length and width as dictionaries
        yield {'width': self.width}    # Yield print one value at a time


rectangle = Rectangle(10, 20)

for item in rectangle: # It yield two dictionaries: one for the length and one for the width.
    print(item)
