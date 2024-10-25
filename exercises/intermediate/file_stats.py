# Exercise 1: File Statistics
# Write a Python program that reads a text file and prints:
# 1. The total number of words.
# 2. The number of unique words.
# 3. The frequency of each word (store the frequencies in a dictionary).
# 4. The longest word in the file.

from collections import defaultdict, Counter

def file_stats(file_name: str):
    
    with open(file_name, "r") as file:
        
        file_content = file.read()
        word_list = file_content.split()
        
        #Number of words
        n_words = len(word_list)
        print(f"The total number of words in the file is: {n_words}")
        
        #Number of unique words
        unique_words = len(set(word_list))
        print(f"The number of unique words is: {unique_words}")
        
        #Frequency of words using defaultdict
        word_freq = defaultdict(int)
        for word in word_list:
            word_freq[word] += 1
        print(f"Word frequency: {dict(word_freq)}")

        #Frecuency using Counter()
        word_frequ = Counter(word_list)
        print(f"Word frequency: {dict(word_frequ)}")

        #Longest word
        print(f"The longest word is: {max(word_list, key = len)}")
        
file_stats("testFile.txt")