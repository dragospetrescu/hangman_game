The simple classic game of hangman for any language implemented in python

Implementation:
  In Linux we search in /usr/share/dict for the dictionary used by the computer.
  We copy it to the location of the game and remove the words that start with
  capital letter and the ones that contain apostrophes.

  We choose a word randomly from the new dictionary. The user has to input a
  letter followed by enter. If the word contains the letter, the string with the
  information gathered by now will be printed. If not, the old string will be
  printed along with the numbers of mistakes.

  Requirements:
    python >= 2
    How to get python:
      sudo apt-get install python

 Installation:  
  Simply run ./hangMan.py or python hangMan
