class factorization:
    
    """
    Factorize two numbes integers with greastest common divisor
    and least common multiple from Euclidean algoritm. 
    Source: Wikipédia
    -------
    Parameters:
        x, y: integers and real
    -------   
    Output:
        number (real)
        
    """
    
    
    def __init__(self, x, y):
     
        if x == 0 and y == 0:
            raise "At least one value must be non-zero."
        elif (isinstance(x, float) or isinstance(y, float)):
            raise "The values must be integer"
            
        self.a = int(x)
        self.b = int(y)
    @property
    def GCD(self):
        
        """
        The greatest common divisor (GCD) of two or more integers,
        which are not all zero, is the largest positive integer that 
        divides each of the integers. For two integers x, y, the 
        greatest common divisor of x and y is denoted 
        gcd(x,y)
        ----
        Example:
         >>>x = 12
         >>>y = 45
         >>>fac = factorization(x, y)
         >>>print(fac.GCD)
            3
        """
        #create a infite loop with 
        while self.a != self.b:
 
            if self.a > self.b:
                self.a = self.a - self.b
            else:
                self.b = self.b - self.a
                
        return self.a
    @property
    def LCM(self):
        
        """
        The least common multiple, lowest common multiple, 
        or smallest common multiple of two integers a and b, 
        usually denoted by lcm(a, b), is the smallest positive 
        integer that is divisible by both a and b. 
        Since division of integers by zero is undefined, 
        this definition has meaning only if a and b are both different 
        from zero. 
        ----
        Example:
         >>>x = 2
         >>>y = 3
         >>>fac = factorization(x, y)
         >>>print(fac.LCM)
            6 
        
        """
    
       # choose the greater number
        if self.a > self.b:
            greater = self.a
        else:
            greater = self.b
    
        while True:
            if((greater % self.a == 0) and 
               (greater % self.b == 0)):
                self.lcm = greater
                break
            greater += 1
    
        return self.lcm


