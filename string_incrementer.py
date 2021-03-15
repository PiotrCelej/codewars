'''
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
'''

def stringIncrementer(strng) :
    word = strng.rstrip("0123456789")
    nmbr = strng[len(word):]
    n=1
    if len(nmbr)>0 :
        n = str(int(nmbr)+1)

    format_string = "{:0>"+str(len(nmbr))+"}"
    return word+format_string.format(n)

print(stringIncrementer('foo12'))
print(stringIncrementer('foo0043'))
print(stringIncrementer('foo100'))
print(stringIncrementer('foobar0001'))
print(stringIncrementer('foo23bar0004'))
