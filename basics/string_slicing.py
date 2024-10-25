#Create a substring from elemets of another string
#indexing[] or slice()
#[start:stop:step]

name = "Matthew Vergara"

first_name = name[0:4]
last_name = name[8:15]
print(first_name)
print(last_name)

reversed_name = name[::-1]
print(reversed_name)

website = "http://www.google.com/"
website2 = "http://www.youtube.com/"

slice = slice(11,-5)

print(website[slice])
print(website2[slice])
