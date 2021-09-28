# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 23:07:04 2021

@author: LuizF
"""

def find_sequence(text, seq):
    """
    Function for to find number of times 
    appears in text (sequemce of letters). 
    Then, if ending '.' (dot) will finish the code. 
    Warning: Overlaps can occur. 
    
    ------
    Parameters:
        Random Sequence of letters (string) 
        Sequence of your choice (string)
    -------        
    Output:
        number of repetions (integer)
    -------
    Example:
        text = "AAABAAAADCAAC"
        seq = "AA"
        print(find_sequence(text, seq))
    >>> 6
    
    """
    
    if '.' not in text:
        text = text + '.'
    
    n = len(seq)
    values = []
    
    for i in range(len(text)):
        word = text[i : i+n]
        if word == seq:
            values.append(word)
        if '.' in word:
            break

    return len(values)


