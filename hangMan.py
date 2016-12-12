#!/usr/bin/env python
# the main function of the program
# import the functions form the other files
from getRandomWord import getRandomWord
from getDictionary import getDictionary
from filterDictionaryWords import filterDictionaryWords
import sys
import os
import os.path

# create the dictionary file
if not os.path.isfile("dictionary"):
    getDictionary ()
    filterDictionaryWords()


# word recieves a random word from the computers dictionary
# found is the file
word = getRandomWord()
found = list (list ('_')*len(word))
os.system('clear')

# make the first and last letter known and all their repetitions
for i in range (0, len(word)):
    if word [i] is word [0]:
        found [i] = word [0]
    elif word [i] is word [-1]:
        found [i] = word [-1]

# read a letter and check if word contains that letter and makes is known
print found
error = 0
while found != word and error < 5:
    letter = (sys.stdin.read(2))[0]
    os.system('clear')
    ok = 0
    for i in range (0, len(word)):
        if word [i] is letter:
            found [i] = letter
            ok = 1
    if ok == 0:
        error += 1;
        print ("Letter was not good. Number of mistakes: "),
        print error
        print found
    else:
        print ("Letter was good the new string is :")
        print found


# Check if win or lose
if error == 5:
    print ("You failed! The word was "),
    print word
else:
    print word
    print ("Congratulations! ")
