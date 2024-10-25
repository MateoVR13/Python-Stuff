#Nesting functions works like in math, the inner function will be resolved first 
#and the returned value is used as the argument for the next outer function.


# num = input("Enter a whole positive number: ")

# num = float(num)
# num = abs(num)
# num = round(num)

num = round(abs(float(input("Enter a whole positive number: "))))

print(num)