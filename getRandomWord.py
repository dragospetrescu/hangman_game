#getRandomWord is a function that generates a random number and then returns the
#corresponding word in the dictionary

import random

def generateNumber ( maxValue ):        #generating random number between 0 and
    return random.randint(0, maxValue)  #maxValue, where maxValue is the number
                                        #line in the input file

def fileLength ( fname ):          #counting the number of the lines in the file
    inputF =  open(fname)
    for i, line in enumerate(inputF):
        pass
    return i + 1

def getRandomWord ( ):
    fileName = "dictionary"
    inputFile = open(fileName)         #open the dictionary file
    maxValue = fileLength( fileName )  #get the number of lines in the input file
    randomValue = generateNumber(maxValue) #get a random number

    for i, line in enumerate(inputFile):
        if (i == randomValue):
            word = line
            break

    listedWord = list(word) #converting the string to a list
    del listedWord[-1]      #deleting the last character (enter)
    inputFile.close()       #closing the file
    return listedWord
