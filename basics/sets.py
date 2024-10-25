#Collection which is unordered, unindexed, and no duplicate values.

utensils = {"Fork","Spoon","Knife","Knife","Knife"}

dishes = {"Bowl","Plate","Cup","Knife"}

# utensils.update(dishes) #Adds elements from another set

# utensils.add("Napkin")

# utensils.remove("Fork")

# #utensils.clear()

# dinner_table = utensils.union(dishes)

print(utensils.difference(dishes))
print(utensils.intersection(dishes))

# for x in dinner_table:
#     print(x)