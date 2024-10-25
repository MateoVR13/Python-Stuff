#index operator [] = gives acces to a sequences's element (str,list,tuples)

name = "matthew VR!"

if(name[0].islower()):
    name = name.capitalize()
    
print(name)


first_name = name[:7].upper()
last_name = name[8:].upper()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)