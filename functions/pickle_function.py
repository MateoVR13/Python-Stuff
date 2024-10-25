
import pickle

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        
    def bark(self):
        print(f"My name is {self.name} and I'm a {self.age} years old {self.breed}")
        
data = Dog("Max", "Golden Retriever", 5)

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
    
with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)
    
print(loaded_data)
loaded_data.bark()