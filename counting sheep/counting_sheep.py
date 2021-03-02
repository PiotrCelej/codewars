data = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

missing_data = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  "null",
  True,  False, False, "True" ,
  True,  True,  True,  True ,
  False, False, True,  True]

def count_sheeps(inData) :
    #check proper values
    output = 0
    for i in inData :
        if type(i) == bool :
            if i : output += 1  
    return output

print("No of sheeps: ",count_sheeps(missing_data))