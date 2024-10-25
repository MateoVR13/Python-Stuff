import math
print("----- Area of a triangle given 3 sides -----")

a = float(input("Enter side a: "))
b = float(input("Enter side b: ")) 
c = float(input("Enter side c: "))

s  = (a+b+c)/2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("The area of the triangle is: ", round(area, 3),"cm")