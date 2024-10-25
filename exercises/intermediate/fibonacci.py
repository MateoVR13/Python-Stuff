# ### **Exercise 7: Fibonacci Sequence**

# - Write a function that generates the Fibonacci sequence up to a certain number of elements.
# - Store the sequence in a list and then write it to a file.
# - Read the file and print the sequence.

def fibonacci_sequence():

    list_a = [0, 1]
    j = 0

    value = int(input("Enter the number of elements to calculate: "))

    for i in range(2, value):
        
        next = list_a[i - 1] + list_a[i - 2]    
        list_a.append(next)


    with open("sequence.txt", "w") as file:
        
        file.write(str(list_a))
        print(f"The sequence has been saved as {file.name}")
        
    with open(file.name, "r") as file:
    
        content = file.read()
        print(content)
        
fibonacci_sequence()