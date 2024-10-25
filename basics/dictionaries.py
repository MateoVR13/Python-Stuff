#Dictionary is a changeable, unordered collection of unique key:value pairs 
#fast beacause they use hashing, allow us to acces a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

# print(capitals.get('Russia'))

# print(capitals.keys())

# print(capitals.values())

# print(capitals.items())
    
capitals.update({'Germany':'Berlin'})

capitals.update({'USA':'Las Vegas'})

for key,value in capitals.items():
    print(key, value)