# function that deletes non-corresponding words (such as names) from the
# dictionary
import os

def filterDictionaryWords ( ):
    fileName = "tempDictionary"
    filteredDict = "dictionary"
    inputFile = open(fileName, "r")         #open the dictionary file
    outputFile = open(filteredDict, "w")


    for tempTuple in enumerate(inputFile):
        line = tempTuple[1]
        if (str(line[0]).isupper() is False and '\'' not in line
                                            and len(line) > 2):
            outputFile.write(str(line))


    inputFile.close()       #closing the input file
    outputFile.close()      #closing the output file
    os.remove(fileName)
