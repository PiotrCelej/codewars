
from math import sqrt


def is_square(n):
    if n<0 : return False
    else :
        if (sqrt(n) % 1) >0 : return False
        else : return True

print ("Test")
print (is_square(0))
print (is_square(-1))
print (is_square(3))
print (is_square(4))
print (is_square(25))