#rozkład liter w słowniku języka polskiego biorąc pod uwagę odmianę słów. Aplikacja ignoruje wielkość liter
import traceback

def countDistrLetters(f) :
    output = {}

    file = open(f, encoding='utf-8')
    errCount = 0
    lineCount = 0

    try :
        for line in file :
            lineCount += 1
            for i in line :
                j = i.lower()
                if str(j) in "1234567890 .,\n" :
                    pass
                else :
                    if j in output :
                        output[j] = output.get(j) +1
                    else :
                        output[j] = 1
    except :
        errCount += 1
        print("Error in reading a letter: ",errCount)
        traceback.print_exc()

    print("Lines read:", lineCount)
    print(output)

    file.close()
    return True

if __name__ == "__main__" :
    countDistrLetters('lettersDistribution/odm.txt')