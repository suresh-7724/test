def is_leap_year(year):
    return (year%4==0 and year %100!=0) or (year%400==0)

def date_match(date_str):
    from datetime import datetime
    year, month,date =map(int, date_str.split('-'))
    if(is_leap_year(year)):
        return "leap year"
    if(month==12 and date==25):
        return "Christmas"
    else:
        return "Regular"
    
date =input("Enter the date in the format YYYY-MM-DD: ")
print(date_match(date))