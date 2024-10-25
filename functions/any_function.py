import os

numbers = [0, 1, 2, 3]
print(any(numbers))

test = []
print(any(test))

numbers2 = [-1, -2, 0, -4]
print(any(num > 0 for num in numbers2))

strings = ["apple", "", "banana"]
print(any(s == "" for s in strings))

file_paths = ["file1.txt", "file2.txt", "file3.txt"]

print(any(os.path.exists(path) for path in file_paths))

