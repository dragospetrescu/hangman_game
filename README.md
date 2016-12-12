The simple classic game of hangman implemented in python in any language

Implementation:
  In Linux we search in /usr/share/dict for the dictionary used by the computer. We copy it to the location of the game and       remove the words that start with capital letter and the ones that contain apostrophes.
  
  We choose randomly from the new dictionary a word. The user has to input a letter followed by enter. if the word contains the   letter the string with the information gathered by now will be printed. if not, the old string will be printed along with the   numbers of mistakes.
  
  Requirments:
    python >2
    to get python:
      sudo apt-get install python
  
 Installation:  
  Simply ./hangMan or python hangMan
