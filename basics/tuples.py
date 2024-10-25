#Collection which is ordered and unchangeable 
#used to group toghether related data

student = ("Matt",25,"Male")
print(student.count("Matt"))
print(student.index("Male"))

for x in student:
    print(x)
    
if "Matt" in student:
    print("Matt is on the list.")
