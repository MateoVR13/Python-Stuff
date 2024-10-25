from collections import Counter

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

count = Counter(words)

print(count)

print(count["apple"])

#Counter function create an object that counts all of the 
#instances/fequencies/specific words/characters or objects
# inside of an iterable object.