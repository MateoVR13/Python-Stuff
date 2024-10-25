#Useful to pack arguments into a tuple so that function 
#can accept a varying amount of arguments

#-------Before--------

def sum(num1, num2):
    add = num1 + num2
    return(add)

print(sum(1,2))


#-------After---------

def adding(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(adding(1,2,3,4))