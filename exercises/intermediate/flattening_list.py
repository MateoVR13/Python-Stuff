# 1. List Flattening
# Problem: Write a function flatten_list(nested_list) that takes a list of lists (which can be of arbitrary depth) and returns a flattened version of the list.
# Example:
# python
# Copy code
# nested_list = [1, [2, [3, [4]], 5], 6]
# # Expected Output: [1, 2, 3, 4, 5, 6]

# nested_list = [1, [2, [3, [4]], 5], 6]

# new_list = []

# for elem in nested_list:
    
#     if type(elem) == list:
        
#         for itm in elem:
            
#             if type(itm) == list:
                
#                 for x in itm:
                                        
#                     if type(x) is list:
                        
#                         for z in x:
#                             new_list.append(z)  
#                     else:
#                         new_list.append(x)    
#             else: 
#                 new_list.append(itm)       
#     else:
#         new_list.append(elem)
    
# print(new_list)   

def flatten_list(nested_list):
    
    new_list = []
    
    for elem in nested_list:
    
        if isinstance(elem, list):
            
            new_list.extend(flatten_list(elem))
    
        else:
            
            new_list.append(elem) 
    
    return new_list

nested_list = [1, [2, [3, [4]], 5], 6]
flattened = flatten_list(nested_list)
print(flattened)
