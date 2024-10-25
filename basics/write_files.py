text = "This is an appended text line."

# Create new file
# with open('auxFiles/test2.txt', 'w') as file:
#     file.write(text)


#Append text to existent file
with open('auxFiles/test2.txt', 'a') as file:
    file.write(text)