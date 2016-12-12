import os
import platform

def getDictionary( ):
    from shutil import copyfile

    if (platform.system() == 'Linux'):
        copyfile(os.path.realpath
        ('/usr/share/dict/words.pre-dictionaries-common'), './tempDictionary')
    else:
         if (platform.system() == 'Windows'):
             pass #TODO: get dictionary from windows
    #else:
        #TODO: unsupported operating system action
