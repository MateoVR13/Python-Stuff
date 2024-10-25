age = int(input("How old are you?: "))


if age == 100:
    print("You're a century old!")
elif age >= 18:
    print("You're an adult.")
elif age < 0:
    print("Wtf?")
else:
    print("You're a child.")