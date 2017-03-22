class Fraction:

    def __init__ (self, top, bot):
        try:
            common = self.gcd(top, bot)
            self.num = top // common
            self.den = bot // common
        except Exception as error:
            raise error

    @staticmethod
    def gcd (num, den):
        while num % den != 0:
            old_num = num
            old_den = den

            num = old_den
            den = old_num % old_den
        return den

    def __eq__ (self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __ne__ (self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum != secondnum

    def __gt__ (self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum > secondnum

    def __ge__ (self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum >= secondnum

    def __lt__ (self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum < secondnum

    def __le__ (self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum <= secondnum

    def __add__ (self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den

        return Fraction(newnum, newden)

    def __sub__ (self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den

        return Fraction(newnum, newden)
    
    def __mul__ (self, other):
        newnum = self.num * other.num
        newden = self.den * other.den

        return Fraction(newnum, newden)

    def __truediv__ (self, other):
        newnum = self.num * other.den
        newden = self.den * other.num

        return Fraction(newnum, newden)

    def __str__ (self):
        return str(self.num) + '/' + str(self.den)

    def getNum (self):
        return self.num

    def getDen (self):
        return self.den

    def show (self):
        print(self.num, '/', self.den)
