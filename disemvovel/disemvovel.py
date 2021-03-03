text = "This website is for losers LOL!"

def disemvovel(txt) :
    vvls = {'a','e','i','o','u'}
    output = ""
    for i in txt :
        if vvls.isdisjoint({str(i).lower()}) :
            output += i
    return output

print(text)
print(disemvovel(text))

