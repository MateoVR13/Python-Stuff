# With a given integral number n, write a program to generate a dictionary that
# contains (i, i*i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.

numb = int(input("Please enter a number: "))

dictio = {}

for num in range(1, numb+1):
    
    dictio[num] = num * num
    
print(dictio)