# Given a dictionary where the keys are dates (as strings)
# and the values are tuples with temperature, humidity, and wind
# speed, write a function that:

# Prints the average temperature for a given month.
# Finds and prints the day with the highest wind speed.

weather_data = {

    "2024-01-01": (15, 80, 12),
    "2024-01-02": (17, 75, 10),
    "2024-01-03": (16, 78, 15),
    "2024-02-04": (14, 85, 8),
    "2024-02-05": (18, 72, 20),
    "2024-02-01": (20, 68, 10),
    "2024-03-02": (22, 65, 12),
    "2024-03-03": (21, 70, 15),
    "2024-03-04": (19, 75, 18),
    "2024-04-05": (23, 60, 10),
    "2024-04-01": (25, 55, 8),
    "2024-04-02": (27, 50, 12),
    "2024-05-03": (26, 60, 10),
    "2024-05-04": (24, 65, 15),
    "2024-05-05": (28, 48, 20),
    "2024-06-06": (13, 90, 10),
    "2024-06-07": (12, 85, 5),
    "2024-06-08": (14, 80, 15),
    "2024-07-06": (21, 66, 14),
    "2024-07-07": (22, 62, 16),
}

def avg_month_temp():

    month_data = []

    sel_month = int(input("Please enter the month number w/o zeros: "))

    for date, values in weather_data.items():

        if int(date[5:7]) == sel_month:
            
            month_data.append(values[0])
    
    print(f"The average temperature for the month {sel_month} is {format(sum(month_data)/len(month_data), ".1f")}°C")   
    
    
    for values in weather_data.values():
        
        print(values[2])     
    
avg_month_temp()