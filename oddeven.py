

def even_or_odd(number):
    try :
        result = number % 2
        if result == 1 :
            return "Odd"
        else :
            return "Even"
    except :
        return ""

print ("Start test")
print (even_or_odd(2))
print (even_or_odd(3))
print (even_or_odd(-123))
print (even_or_odd(2.34))
print (even_or_odd(0.33))
print (even_or_odd("kiszka"))
print (even_or_odd())

