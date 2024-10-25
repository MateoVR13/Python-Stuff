# Write a fizzBuzz() function with a single integer parameter named upTo. For the numbers 1
# up to and including upTo, the function prints one of four things:
# Prints 'FizzBuzz' if the number is divisible by 3 and 5.
# Prints 'Fizz' if the number is only divisible by 3.
# Prints 'Buzz' if the number is only divisible by 5.
# Prints the number if the number is neither divisible by 3 nor 5.

def fizzBuzz(upTo: int):

    for numb in range(1, upTo + 1):

        if numb % 3 == 0 and numb % 5 == 0:
            print("FizzBuzz", end=" ")
        elif numb % 3 == 0:
            print("Fizz", end=" ")
        elif numb % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(numb, end=" ")


inp_numb = int(input("Please enter a number: "))
fizzBuzz(inp_numb)