#break = to terminate the loop entirely
#continue = skips to the next iteration of the loop
#pass = does nothing, acts as a placeholder

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phone_number = "313-496-7194"

# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

for i in range(1,15):
    if i == 13:
        pass
    else:
        print(i, end="-")