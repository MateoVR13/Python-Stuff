#Complete the function to find the count of the most frequent item of an array. You can
#assume that input is an array of integers. For an empty array return 0

input_int = list(input("Please enter a positive integer: "))

freq_numb = max(set(input_int), key=input_int.count)

count_freq_numb = input_int.count(freq_numb)

print(f"The most frequent number is {freq_numb} which repeats {count_freq_numb} times.")