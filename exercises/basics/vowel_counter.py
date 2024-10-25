string = input("Please enter a string: ")
counter = 0
vowels = ["a","e","i","o","u"]

for i in string:
    if i in vowels:
        counter = counter+1

print("Theres's ", str(counter), " vowels in the string.")