# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 23:28:20 2021

@author: LuizF
"""

def histogram(sequence, symbol = True):
    
    """
    Histogram is a graphical representation of the frequency 
    distribution, very common when we need to analyze sample data. 
    In this histogram implementation can to read a list of integers 
    between 0 and 100 and print a histogram of the frequency of each number.

    ------
    Parameters:
        sequence: list of integers  
        symbol = returns the frequency like '#' (defoult = True)
    -------
    Output:
        list of tuples like (number, frequency)
    -------
    Example:       
        seq =  [5, 5, 7, 8, 10, 6, 5, 6, 6, 7, 4, 5, 7, 6, 6, 7, 6, 6]
        print(histogram(seq, symbol = True))
    >>> [(4, '#'), (5, '####'), (6, '#######'), (7, '####'), (8, '#'), (10, '#')]
    
    """
    
    #Create a dictonary to count values in the sequence
    out_count = {x: sequence.count(x) for x in sequence if x > 0}
    
    dict_values = {k: v for k, v in sorted(out_count.items(), 
                                           key=lambda item: item[0])}
    
    hist = []
    for index, key in zip(dict_values.keys(), 
                          dict_values.values()):
        if symbol == True:
            result = (index, "#" * key)
        else:
            result = (index, key)
        hist.append(result)

    return hist    

