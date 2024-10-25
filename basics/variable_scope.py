var = "Matt" #Global scope makes the variable value available inside and outside functions

def printName():
    var = "Mateo" #Local scope makes the variable value available only inside this function
    print(var)
    
printName()
print(var)