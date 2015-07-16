__author__ = 'liuhui'

def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])


def reversestr(str):
    if str == "":
        return ""
    else:
        return str[-1] + reversestr(str[:-1])

def removeWhite(s):
    if s == "":
        return ""
    else:
        if s[0] not in "abcdefghiklmopqrstuvwxyz":
            return removeWhite(s[1:])
        else:
            return s[0] + removeWhite(s[1:])

def isPal(s):
    if len(s) == 0  or len(s) == 1:
        return True
    else:
        if s[0] == s[-1]:
            return isPal(s[1:-1])
        else:
            return False

import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, t)
        t.left(40)
        tree(branchLen-15, t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(120,t)
    myWin.exitonclick()




# for testing
# print(listsum([1,3,5,7,9]))
# print(reversestr("hello"))

# print(removeWhite("madam i'm adam"))
#
# print(isPal(removeWhite("x")))
# print(isPal(removeWhite("radar")))
# print(isPal(removeWhite("hello")))
# print(isPal(removeWhite("")))
# print(isPal(removeWhite("hannah")))
# print(isPal(removeWhite("madam i'm adam")))

# drawSpiral(myTurtle,100)
# myWin.exitonclick()

main()