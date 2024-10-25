# Write a program which accepts a sequence of comma-separated numbers
# from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')


inp_str = str(input("Please enter the number sequence of comma-separated numbers: "))

sep = inp_str.split(",")
tup = tuple(sep)
lis = list(sep)

print(lis)
print(tup)