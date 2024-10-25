#PYTHON BASICS REVISION

#Numerical --------------------------------------------------

#int
int_a = 23

print(int_a + 2)

#float 
float_a = 324.157216837612

print(format(float_a, ".5f"))

#complex
complex_a = 3j

print(complex_a * 2)


#Text -------------------------------------------------------

#strings

str_a = "Mateo Vergara Roa"
str_b = "Data Science"
str_c = str_a + " studies " + str_b
print(str_c)

str_d = "Hi!"
str_e = "This is the year"
int_b = 2024
float_b = 23.5
print(f"{str_d}{str_e} {int_b} and is {float_b}ºC.")


#Collections of Data (lists, tuples, sets, dictionaries) ---

#lists: are mutable, ordered, can contain duplicates and any 
#data type including other lists, these are defined by square
#brackets[].

list_a = [1, 2, 3, 4, [11, 22, 33], 5, 6]

#We can access nested lists by the use of [][] indicating the
#position in the main list and then the nested one.

print(list_a[4][1])

list_a.append(7)

print(list_a)

list_a.remove(5)

print(list_a)

#tuples: ordered, unmutable and allow duplicated values. We
#can't add or remove items after being created. These are
#defined by parentheses ().

tuple_a = ("mateo", "vergara", "roa")
print(tuple_a)

#sets: unordered, unmutable and unindexed. Items are
#unchangeable and do not allow duplicate values, but you can
#remove items and add new items. Sets are written with curly
#brackets {}

set_a = {"Python", "SQL", "Excel", "Python", "Power BI"}
print(set_a)

set_a.remove("Power BI")
print(set_a)

#dictionaries: are used to store data values in key:value pairs.
#A dictionary is a collection which is unordered, changeable and 
#do not allow duplicates (keys). Dictionaries are written with 
#curly brackets {:}, and have keys and values

dict_a = {
    
    "name":"Mateo",
    "surname":"Vergara",
    "age":25,
    "skills": ["Python", "SQL", "R"]
}

print(dict_a)

#We can also print single values:

print(dict_a["name"])