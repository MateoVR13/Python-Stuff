#**kwargs will pack arguments into a dictionary 
#it makes a function accept a varying amount of 
#keyword arguments

#-------------Before-------------------

def hello(first, last):
    print("Hello " + first +" "+ last)
    
hello(first="Mateo", last="Vergara")

#--------------After-------------------

def hi(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end = " ")

hi(title = "Mr." ,first1 = "Matthew", middle = "John", last1 = "VR")