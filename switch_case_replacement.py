"""
In Python, there is no Switch - Case code. Instead, we can define it using dictionaries.
"""
def week(d):
    switcher = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
    }
    
    return switcher.get(d, "Invalid input")


print(week(3))