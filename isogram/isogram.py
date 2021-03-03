#is_isogram("Dermatoglyphics" ) == true
#is_isogram("aba" ) == false
#is_isogram("moOse" ) == false # -- ignore letter case

def is_isogram(text) :
    outSet = set()
    for i in text :
        outSet.add(str(i).upper())
    if len(text) == len(outSet) : return True
    else : return False

print(is_isogram("Dermatoglyphics" ))
print(is_isogram("aba" ))
print(is_isogram("moOse" ))
