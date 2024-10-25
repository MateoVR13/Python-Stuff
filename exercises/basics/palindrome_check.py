string = input("Please enter a string: ")

if string == string[::-1]:
    print("The word is plaindrome.")
else:
    print("The word is not palindrome.")