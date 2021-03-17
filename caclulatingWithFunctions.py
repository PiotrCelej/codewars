'''
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))

'''

def plus(num=0) : return "+"+str(num)

def minus(num=0) : return "-"+str(num)

def times(num=1) : return "*"+str(num)

def divided_by(num=1) : return "//"+str(num)

def zero(calc="") : 
    if calc == "" : return 0
    else : return eval(str("0"+calc))

def one(calc="") :
    if calc == "" : return 1
    else : return eval(str("1"+calc))

def two(calc="") :
    if calc == "" : return 2
    else : return eval(str("2"+calc))

def three(calc="") :
    if calc == "" : return 3
    else : return eval(str("3"+calc))

def four(calc="") :
    if calc == "" : return 4
    else : return eval(str("4"+calc))

def five(calc="") :
    if calc == "" : return 5
    else : return eval(str("5"+calc))

def six(calc="") :
    if calc == "" : return 6
    else : return eval(str("6"+calc))

def seven(calc="") :
    if calc == "" : return 7
    else : return eval(str("7"+calc))

def eight(calc="") :
    if calc == "" : return 8
    else : return eval(str("8"+calc))

def nine(calc="") :
    if calc == "" : return 9
    else : return eval(str("9"+calc))

print(seven(times(five()))) # must return 35
print(four(plus(nine()))) # must return 13
print(eight(minus(three()))) # must return 5
print(six(divided_by(two()))) # must return 3
print(eight(divided_by(three()))) # must return 2

# print(two(divided_by(zero())))

print(times(five()))