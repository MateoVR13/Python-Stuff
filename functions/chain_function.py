from itertools import chain

#List addition

list_1 = [1, 2, 3]
list_2 = ["a", "b", "c"]

combined_add = list_1 + list_2 #Immediate memory-intensive, this
#will create a new list containg all the values, all this values
#are going to be stored in memory even when not needed.

#itertools.chain
combined_chain = list(chain(list_1, list_2)) #Lazy and efficient
#this will create an iterator that will step over the values from
#list 1 and list 2. This values will be accessible only when we
#actually need them

print(next(combined_chain)) 
#The function next gives the next value of an iterable value
#remove the list() function from previous line to test it out
print(combined_add)
print(combined_chain)


#Conclusion: Using chain() reduces memory use, allowing to call
#values when needed instead of while execution 