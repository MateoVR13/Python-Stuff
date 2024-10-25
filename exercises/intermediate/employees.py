# Create a list of employee dictionaries with the following keys: "name", "age", and "position".
# Write a function to promote an employee by changing their position and increasing their age by one year.
# Allow the user to search for an employee by name and then promote them if found.

from pprint import pprint

empl_list = [{"name": "John",
              "age": 43,
              "position": "Manager",}, 
             
             {"name": "Annie",
              "age": 27,
              "position": "Marketing Representative",},
              
             {"name": "Steven",
              "age": 33,
              "position": "HR Representative",}
            ]

def promote_employee():
    
    print(f"Which employee do you wish to promote?")
                
    employee_names = [empl["name"] for empl in empl_list]
    pprint(employee_names)
                
    employee = str(input("Please enter the employee's name to promote: "))
    
    found = False
    
    for value in range(0, len(empl_list)):
        
        if empl_list[value]["name"] == employee:
            
            emp_position = str(input("Please enter the employee's new position: "))
            
            empl_list[value]["position"] = emp_position
            empl_list[value]["age"] += 1
    
            pprint(empl_list[value])
            found = True
            break
        
    if not found :
        
        print("Employee not found in database!")
    
promote_employee()