__author__ = 'liuhui'

def gcd(m, n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn

    return n

class Fraction:

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    def setNum(self,num):
        self.num = num

    def setDen(self,den):
        self.den = den

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __add__(self, otherFraction):
        newNum = self.num*otherFraction.den + self.den*otherFraction.num
        newDen = self.den * otherFraction.den
        common = gcd(newNum, newDen)

        return Fraction(newNum//common, newDen//common)

    def __eq__(self, otherFraction):
        firstM = self.num * otherFraction.den
        secondM = self.den * otherFraction.num

        return firstM == secondM

    def __sub__(self, otherFraction):
        newNum = self.num*otherFraction.den - self.den*otherFraction.num
        newDen = self.den * otherFraction.den
        common = gcd(newNum, newDen)

        return Fraction(newNum//common, newDen//common)

    def __mul__(self, otherFraction):
        newNum = self.num * otherFraction.num
        newDen = self.den * otherFraction.den
        common = gcd(newNum, newDen)

        return Fraction(newNum//common, newDen//common)

    def __truediv__(self, otherFraction):
        newNum = self.num*otherFraction.den
        newDen = self.den*otherFraction.num
        common = gcd(newNum, newDen)

        return Fraction(newNum//common, newDen//common)

def main():
    x = Fraction(1,2)
    y = Fraction(2,3)

    print(x + y)
    print(x == y)
    print(x-y)
    print(x*y)
    print(x.__truediv__(y))

main()