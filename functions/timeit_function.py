import timeit

#This function allows to time how long 
#certain code takes to run

#Implementation 1: List Comprehension

code_1 = """
a = [1, 2, 3, 4, 5]
b = [x * 2 for x in a]
"""

#Implementation 2: Map function

def code_2():
    a = [1, 2, 3, 4, 5]
    b = list(map(lambda x : x * 2, a))
    
#Time both implementations (we can pass a function or a string to evaluate)

time_1 = timeit.timeit(code_1, number = 100000) #By default runs 1 Million times
time_2 = timeit.timeit(code_2, number = 100000)

print(f"List comprehension time: {time_1}")
print(f"List comprehension time: {time_2}")