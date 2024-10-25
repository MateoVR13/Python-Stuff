# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

from dataclasses import dataclass

@dataclass
class TestClass():
    
    inp = ""
    
    def get_string(self):
        
        self.inp = input("Enter a string: ")
        
    def print_string(self):
        
        print(self.inp)
        
test = TestClass()
test.get_string()
test.print_string()