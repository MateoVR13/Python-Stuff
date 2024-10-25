
from collections import defaultdict

words = ["apple","banana","apple","orange","banana","apple"]
word_count = defaultdict(int)

for word in words:
    word_count[word] += 1
    
print(dict(word_count))