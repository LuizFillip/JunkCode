def fill_nans(y1, value = None):
    """Complete value in list"""
    for num in range(len(y1) - 1):
        if value is None:
            if y1[num] != y1[num]:
                y1[num] = y1[num - 1]
        else:
            if y1[num] != y1[num]:
                y1[num] = value
            
    return y1