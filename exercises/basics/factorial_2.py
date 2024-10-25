# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single
# line.
# Suppose the following input is supplied to the program: 
# 8
# Then, the output should be:
# 40320

def factorial_2(numb: int):
    
    j = 1
    
    for n in range(1, numb+1):
        
        j = j*n
        
        
    print(j)
 
factorial_2(8)