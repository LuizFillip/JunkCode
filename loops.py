lenght = 19
import numpy as np

for i in range(lenght):
    for j in range(lenght):
        if j % 2 == 0:
            if (j >= (abs(4 - i) * 2 - 1)):
                print(j + 2, end = "")
            else:
                print(" ", end = "")
        else:
            print(" ", end = "")
    print()
    
def replace_by_limits(array, limit):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if (array[i][j] > limit) or (array[i][j] < -limit):
                array[i][j] = np.nan
            
    return(array)

