
def isTriangle(a,b,c) :
    if a+b <= c : return False
    elif a+c <= b : return False
    elif c+b <= a : return False
    else : return True

print(isTriangle(1,2,5))
print(isTriangle(1,4,5))
print(isTriangle(3,3,5))
print(isTriangle(10,6,5))
