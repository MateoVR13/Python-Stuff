### **Exercise 4: Password Strength Checker**

# - Write a function that takes a password string as input and returns a strength rating:
#     - "Weak" if the password is less than 6 characters or only contains letters.
#     - "Medium" if the password contains both letters and numbers.
#     - "Strong" if it contains letters, numbers, and special characters.
# - Use chained operators in your conditionals.


def pass_check(passw: str ):
    
    spc_chars = "! # $ % & ' ( ) * + , - . / : ; < = > ? @ [ ] ^ _ ` { | } ~ "
    char_list = spc_chars.split(" ")
    has_alnum = any(char.isalnum() for char in passw)
    
    if len(passw) < 6 and  passw.isalpha() == True:
        
        print("Weak password strength!")
        
    elif passw.isalnum() == True:
        
        print("Medium password strength")
            
    elif has_alnum and any(char in passw for char in char_list):
        
        print("Strong Password!")

        
pass_check("#ma4teo1")