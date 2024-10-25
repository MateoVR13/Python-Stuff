def calculate_salary(base_salary, bonus_rate = .1):
    
    """
    --------------------------------------------------------------
    
    Calculate the total salary based on the base salary and bonus.
    
    Args:
        base_salary (float): The base salary.
        bonus_rate (floar): The bonus rate. Default is .1.
        
    Returns:
        float: The total salary.
    
    """
    
    return base_salary * (1 + bonus_rate)


def calculate_bonus(total_salary, base_salary):
    return (total_salary- base_salary) / base_salary