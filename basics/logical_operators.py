#Check if two or more conditional statements are trure

#and, or, not

temperature = float(input("What is the temperature outside?: "))

if temperature >= 0 and temperature <= 20:
    print("It's cold outisde.")
    print("It's still safe to go outside.")

elif temperature < 0 or temperature > 30:
    print("Dangerous temperature to go outside.")
    print("Stay inside.")