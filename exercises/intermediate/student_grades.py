# Create a list of student dictionaries, each containing the student's name and their grades in three subjects.
# Write a function that calculates and adds the average grade for each student.
# Use a loop to determine the student with the highest average and print their name and average.

student_list = [
    {"name": "Tim", "grades": {"Chemistry": 4.3, "Biology": 3.8, "Math": 3.5}},
    {"name": "Jhon", "grades": {"Chemistry": 4.0, "Biology": 3.1, "Math": 3.2}},
    {"name": "Andrew", "grades": {"Chemistry": 3.9, "Biology": 4.2, "Math": 3.9}},
]

def average_grade():
    
    max_avg: float = 0.0
    
    for student in student_list:
        
        grades = student["grades"]
        avg_grd = float(format(sum(grades.values())/len(grades.values()), ".1f"))
        student["average"] = avg_grd

        if student["average"] > max_avg:
            
            max_avg = student["average"]
            student_name = student["name"]
    
    print(f"{student_name} has the highest grade average with {max_avg}")
        
average_grade()