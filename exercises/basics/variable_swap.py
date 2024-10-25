a = int(input("Please enter variable 1 value: "))
b = int(input("Please enter variable 2 value: "))

def varSwap(a, b):
    print("Var 1 original value: ", a)
    print("Var 2 original value: ", b)
    
    aux = a
    a = b
    b = aux
    
    print("Var 1 new value: ", a)
    print("Var 2 new value: ", b)

varSwap(a, b)
    
    