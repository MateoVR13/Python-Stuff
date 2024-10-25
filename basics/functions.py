#Function: Block of code which is executed only when it is called.

# def hello(name):
#     print("Hello " + name)

# name = "Judas"
# hello(name)

def hello(name1, last1, char, year):
    print("Hello " + name1 + " " + last1 + char)
    print("Founded in "+ str(year))

name1 = "Judas"
last1= "Priest"
char = "!"
year = 1969
hello(name1, last1, char, year)