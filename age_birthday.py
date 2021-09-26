# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 22:33:25 2021

@author: LuizF
"""

def age_birthday(year, 
                 month, 
                 day, 
                 date_choice = None):
    
    """
    Convert the year (date) of birth of a person and returns 
    how many years he was in 2020 or another day of your choice. 
    --------
    Parameters:
        year: integer
            The smallest and largest year number 
            allowed it's 1 and 9999, respectively 
        month: integer
            Range of 1 to 12 (january to december)
        day: integer
            Range of 1 to 31 (according with each month)
        date_choice: None (defoult, i.e., date today)
                    tuple (i. e, year, month, day) 
            Specify an date which you want compute the years, 
            if None the program get the today date, else
            you can put a specific date
    --------
    Output:
        age: integer
    ------
    Example:
        year = 1994
        month = 12
        day = 26
        print(age_birthday(year, month, day)) 
    >>> the person will turn 27 years old in 2021            
    """
    
    #import "datetime" library and give a nickname 'dt'
    import datetime as dt
    
    #condition for defoult
    if date_choice == None:
        date_today = dt.date.today()
    else:
        #get elements from date choice
        date_today = dt.date(date_choice[0], 
                             date_choice[1], 
                             date_choice[2]) 
    
    #compute de result date
    result_date = date_today - dt.date(year, month, day)
    
    #get values of days and use a floor division for compute the age
    age = result_date.days // 365 + 1
    
    return f"the person will turn {age} years old in {date_today.year}"


print(age_birthday.__doc__)