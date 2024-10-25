#Statement that executes as long as it's condition remains true

name = ""

while len(name) == 0:
    name = input("Enter your name!: ")
    
print("Hello " + name)

while not name:
    name = input("Enter your name!: ")
    
print("Hello " + name)