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
    outTab = ["",""]
    nums = "0123456789"
    l_num = True
    for i in reversed(strng) :
        if i in nums and l_num :
            outTab[1] = outTab[1] + i
        else :
            outTab[0] = outTab[0] + i
            l_num = False
    word = ""
    nmbr = ""
    for j in reversed(outTab[0]) :
        word += j
    for k in reversed(outTab[1]) :
        nmbr +=k
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
