__author__ = 'liuhui'

'''Stack implementation
'''
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, x):
        self.items.append(x)

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def pop(self):
        return self.items.pop()

''' Stack application
'''
def revstring(mystr):
    liststack = Stack()
    liststr = list(mystr)

    for item in liststr:
        liststack.push(item)

    newStr = ""
    while not liststack.isEmpty():
        newStr = newStr + liststack.pop()

    return newStr

def checkOpen(str):
    if str == "(" or str == "{" or str == "[":
        return True
    else:
        return False

def checkMatch(stc, str):
    if str == ")" and stc.peek() == "(":
        return True
    elif str == "}" and stc.peek() == "{":
        return True
    elif str == "]" and stc.peek() == "[":
        return True
    else:
        return False

def parChecker(symbolString):
    balcanceStack = Stack()
    listSym = list(symbolString)

    for item in listSym:
        if checkOpen(item):
            balcanceStack.push(item)
        else:
            if balcanceStack.isEmpty() or not checkMatch(balcanceStack,item):
                return False
            else:
                balcanceStack.pop()

    if balcanceStack.isEmpty():
        return True
    else:
        return False


def parChecker2(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

def divideBy2(decNumber):
    binaryStack = Stack()
    strPrint = ''

    while decNumber > 0:
        binaryStack.push(decNumber%2)
        decNumber = int(decNumber//2)

    while not binaryStack.isEmpty():
        strPrint = strPrint + str(binaryStack.pop())

    return strPrint

def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"
    binaryStack = Stack()
    strPrint = ''

    while decNumber > 0:
        binaryStack.push(decNumber%base)
        decNumber = int(decNumber//base)

    while not binaryStack.isEmpty():
        strPrint = strPrint + digits[binaryStack.pop()]

    return strPrint


def infixToPostfix(infixexpr):
    operatorPrec = {}
    operatorPrec["^"] = 4
    operatorPrec["*"] = 3
    operatorPrec["/"] = 3
    operatorPrec["+"] = 2
    operatorPrec["-"] = 2
    operatorPrec["("] = 1

    operatStack = Stack()
    outputRe = []
    toProceed = infixexpr.split()

    strChr = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
    strNum = "0123456789"

    for elem in toProceed:
        if elem in strChr or elem in strNum:
            outputRe.append(elem)
        elif elem == "(":
            operatStack.push(elem)
        elif elem == ")":
            while operatStack.peek() != "(":
                outputRe.append(operatStack.pop())
            operatStack.pop()
        else:
            while (not operatStack.isEmpty()) and operatorPrec[operatStack.peek()] >= operatorPrec[elem]:
                outputRe.append(operatStack.pop())
            operatStack.push(elem)

    while not operatStack.isEmpty():
        outputRe.append(operatStack.pop())

    return " ".join(outputRe)

# postfix evaluation funtions
def postfixEval(postfixExpr):

    operatStack = Stack()
    toProceed = postfixExpr.split()

    for elem in toProceed:
        if elem in "0123456789":
            operatStack.push(elem)
        else:
            oper2 = operatStack.pop()
            oper1 = operatStack.pop()

            re = doMath(oper1,oper2, elem)
            operatStack.push(re)

    return operatStack.pop()

def doMath(operand1, operand2, operator):
    operand1 = int(operand1)
    operand2 = int(operand2)
    if operator == "+":
        rep = operand1 + operand2
    elif operator == "-":
        rep = operand1 - operand2
    elif operator == "*":
        rep = operand1 * operand2
    elif operator == "/":
        rep = operand1 / operand2

    return rep

'''Stack testing
'''
import timeit
# a = revstring("Hello world")
# print(a)
# test1 = timeit.Timer("revstring(\"Hello world\")", "from __main__ import revstring")
# print("test1 start", test1.timeit(1000))
#
# test2 = timeit.Timer("parChecker('((()))')", "from __main__ import parChecker")
# print("test2 start", test2.timeit(1000))
# test3 = timeit.Timer("parChecker('(()')", "from __main__ import parChecker")
# print("test3 start", test3.timeit(1000))
# test4 = timeit.Timer("parChecker('{{([][])}()}{{([][])}()}{{([][])}()}{{([][])}()}{{([][])}()}{{([][])}()}{{([][])}()}{{([][])}()}{{([][])}()}{{([][])}()}')", "from __main__ import parChecker")
# print("test4 start", test4.timeit(1000))
# test5 = timeit.Timer("parChecker('[{()]')", "from __main__ import parChecker")
# print("test5 start", test5.timeit(1000))
#
# test6 = timeit.Timer("parChecker2('{{([][])}()}{{([][])}()}{{([][])}()}{{([][])}()}{{([][])}()}{{([][])}()}{{([][])}()}{{([][])}()}{{([][])}()}{{([][])}()}')", "from __main__ import parChecker2")
# print("test6 start", test6.timeit(1000))
# test7 = timeit.Timer("parChecker2('[{()]')", "from __main__ import parChecker2")
# print("test7 start", test7.timeit(1000))
# print(divideBy2(42))
# print(baseConverter(25,2))
# print(baseConverter(250,16))
# print(baseConverter(25,8))
# print(baseConverter(256,16))


# print(infixToPostfix("A * B + C * D"))
# print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
# print(infixToPostfix("( A + B ) * ( C + D )"))
# print(infixToPostfix("( A + B ) * C"))
# print(infixToPostfix("A + B * C"))
# print(infixToPostfix("5 * 3 ^ ( 4 - 2 )"))

# print(postfixEval('7 8 + 3 2 + /'))