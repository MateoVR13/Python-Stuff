import os

path = "C:\\Users\\matth\\Dev\\Python\\PythonBasics\\auxFiles\\test.txt"

if os.path.exists(path):
    print("Path location exists.")
    
    if os.path.isfile(path):
        print("That is a file.")
        
    elif os.path.isdir(path):
        print("That is a directory.")
else:
    print("Path location does not exists.")