def celToFah(celsius):
    fahrenheit = (celsius*1.8+32)
    print(celsius,"C°", " is equal to ", fahrenheit,"F°")

def fahToCel(fahrenheit):
    celsius = ((fahrenheit-32)/1.8)
    print(fahrenheit,"F°", " is equal to ", celsius,"C°")

print("----- Temperature Conversor -----")
print("Choose 1 to convert from C° to F°")
print("Choose 2 to convert from F° to C° \n")

while True:
    
    selection = int(input("Enter your selection: "))

    if selection == 1:
        print("\nConverting C° to F°...\n")
        celToFah(float(input("Please enter the temperature in C°: ")))
        break
    
    elif selection == 2:
        print("\nConverting F° to C°...\n")
        fahToCel(float(input("Please enter the temperature in F°: ")))
        break
    
    else:
        print("Please enter a valid option.")