chain = []

while True:
    
    decimal = int(input("\nPlease enter a whole positive number: "))
    
    if decimal < 1:
        
        print("\nInvalid number! Enter a whole positive number.")
    
    else:    
        while decimal >= 1:
            
            value = decimal%2
            chain.append(value)
            decimal //= 2

        for data in reversed(chain):
            print(data, end=" ")
        break