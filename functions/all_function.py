numbers = [1, 2, 3, 4]
print(all(num > 0 for num in numbers))

strings = ["apple", "banana", "cherry"]
print(all(len(s) > 3 for s in strings))