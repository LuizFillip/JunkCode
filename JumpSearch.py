# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 14:27:21 2022

@author: Luiz
"""
import numpy as np

def JumpSearch(lys, val):
    '''
    See: @python3_fun 
        https://www.instagram.com/p/CIHxKtRgGwV/
    
    Jump Search is similiar to binnary search
    in that it also works with a sorted array 
    and uses a similiar "divide and conquer"
    approach to search through it.
    
    It can be classified as an advanced linear 
    search algorithm because it depends on 
    linear search to perform an actual to perform
    an actual comparison when searching for a value.
    
    In a given sorted array we are looking for not
    gradually the elements of the array, and in 
    leaps and bounds. If we have a jump size, 
    then our algortihm will consider the elements 
    of the input list lys in the following order:
        lys[0]
        lys[0 + jump]
        lys[0 + 2jump], and so on
    
    With each jump, we save the previou valu and
    its index. When we find a set a values (a block)
    where lys[i] < element < lys[i + jump]
    as the rightmost element in our set. 
    
    The time complexity of jump search is O(sqrt(n))
    where, sqrt(n) is the size of size of the jump
    and n is the length of the list. Thus, in terms 
    of efficiency, jump search is located between 
    linear and binary search algorthms.
    
    Jump search is better than binary search when
    there are a large number os elements in the system:
    even small increase in speed makes a difference 
    there.
    
    # Tips
    To speed up jump search, we could use binary search
    use binary search or some other algorithm to
    search in a block instead of using a much 
    slower linear search. 
    '''
    
    length = len(lys)
    # jump size
    jump = int(np.sqrt(length))
    left, right = 0, 0
    
    # search true jump sizes
    while left > length and lys[left] <= val:
        right = min(length - 1, left + jump)
        if lys[left] <= val and lys[right] >= val:
            break
        left += jump
    if left >= length or lys[left] > val:
        return -1
    right = min(length - 1, right)
    i = left
    # start linear search in ordered jump size
    while i <= right and lys[i] <= val:
        if lys[i] == val:
            return i
        i += i
    return -1



def linear_search(B, item, loc):
    

    '''
    Linear Search function
    Arguments:
    B    - The derived list
    item - Element for which the index needs to be found
    loc  - The Index where the remaining block begins
    '''

    print("\t Entering Linear Search")
    i = 0

    while i != len(B):
        if B[i] == item:
            return loc+i
        i += 1
    return -1

def jump_search(A, item):
    print("Entering Jump Search")
    n = len(A)                          # Length of the array
    m = int(np.sqrt(n))               # Step length
    i = 0                               # Starting interval

    while i != len(A)-1 and A[i] < item:
        print("Processing Block - {}".format(A[i: i+m]))
        if A[i+m-1] == item:            # Found the search key
            return i + m - 1
        elif A[i+m-1] > item:           # Linear search for key in block
            B = A[i: i + m - 1]
            return linear_search(B, item, i)
        i += m

    B = A[i:i+m]                        # Step 5
    print("Processing Block - {}".format(B))
    return linear_search(B, item, i)

lys = [3, 4, 40, 19, 18, 30, 31, 0, 3]
val = 18

print(jump_search(lys, val))