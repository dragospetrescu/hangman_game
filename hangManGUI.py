from Tkinter import *
from getRandomWord import getRandomWord
from getDictionary import getDictionary
from filterDictionaryWords import filterDictionaryWords
import sys
import os
import os.path


def onKeyPress(event):
    letter = event.char
    ok = 0
    for i in range (0, len(word)):
        if word [i] is letter:
            found [i] = letter
            ok = 1
    if ok == 0:
        wrong_letters.append (letter)



# create the dictionary file
if not os.path.isfile("dictionary"):
    getDictionary ()
    filterDictionaryWords()


# word recieves a random word from the computers dictionary
# found is the file
word = getRandomWord()
found = list (list ('_')*len(word))

# make the first and last letter known and all their repetitions
for i in range (0, len(word)):
    if word [i] is word [0]:
        found [i] = word [0]
    elif word [i] is word [-1]:
        found [i] = word [-1]

wrong_letters =[]
error = 0

# create window and define events
root = Tk()
root.geometry('1000x1000')

label_err = Label (root, text ="Number of errors: "+ str(error))
label_err.config(font=("Courier", 20))
label_err.place(anchor="e")
label_err.pack()

label_wrong = Label (root, text ="Errors: "+ str(wrong_letters))
label_wrong.config(font=("Courier", 20))
label_wrong.place(anchor="e")
label_wrong.pack()


label_found = Label (root, text = found)
label_found.config(font=("Courier", 44))
label_found.place(anchor="center")
label_found.pack()
root.bind('<KeyPress>', onKeyPress)
while found != word and error < 5:
    label_found.config(text=found)
    label_wrong.config(text ="Errors: "+ str(wrong_letters))
    error = len(wrong_letters)
    label_err.config(text ="Number of errors: "+ str(error))
    root.update()
if found == word:
    label_wrong.config(text ="Congratulations, you did it!")
else:
    label_wrong.config(text ="You lost! The word was:")
root.mainloop();
# read a letter and check if word contains that letter and makes is known
