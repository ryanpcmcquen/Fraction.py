class Fraction:

    def __init__ (self, top, bottom):
        self.num = top
        self.den = bottom
    
    @staticmethod
    def gcd (num, den):
        while num % den != 0:
            old_num = num
            old_den = den
            
            num = old_den
            den = old_num % old_den
        return den

    def reduce (self, num, den):
        common = self.gcd(num, den)
        return Fraction(num // common, den // common)
    
    def __eq__ (self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        
        return firstnum == secondnum
    
    def __gt__ (self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        
        return firstnum > secondnum

    def __lt__ (self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        
        return firstnum < secondnum
        

    def __add__ (self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        
        return self.reduce(newnum, newden)

    def __sub__ (self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        
        return self.reduce(newnum, newden)
    
    def __mul__ (self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        
        return self.reduce(newnum, newden)

    def __truediv__ (self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        
        return self.reduce(newnum, newden)

    def __str__ (self):
        return str(self.num) + '/' + str(self.den)

    def show (self):
        print(self.num, '/', self.den)
