from dataclasses import dataclass

#It's a decorator that automatically implements some
#methods that are common while writing a dataclass
#one of them being the __init__ method and __repr__

@dataclass
class Person:
    name: str
    age: int
    job: str
    
    
person_a = Person(name = "Alice", age = 23, job = "Mathematician")
print(person_a)

print(person_a.__repr__)

# A normal class would look like this:
""" class Person:
    
    def __init__(self, name: str, age: int, job: str):
        
        self.name = name
        self.age = age
        self.job = job """