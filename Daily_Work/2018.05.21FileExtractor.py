__author__ = 'Megatron_chen'


'''
From a top directory, extract all files of a specified extension name(or severals in a tuple)
from the top directory and all its subdictionary to a target directory by copying all the files
'''


import os
import os.path
import shutil
import tkinter
from tkinter.filedialog import askdirectory


TopDir = askdirectory(title='Choose the Top directory')
TargetDir = askdirectory(title='Choose the Target directory')
Target_FileExtension = ('.jpg','.jpeg')

Filecount = 0
TopDir_Tree_Generator = os.walk(TopDir)
for EachPiece in TopDir_Tree_Generator:
    if len(EachPiece[2]):
        for EachFile in EachPiece[2]:
            if EachFile.endswith(Target_FileExtension):
                shutil.copy(os.path.join(EachPiece[0],EachFile),TargetDir)
                Filecount += 1

print('Extraction Done! Totally {0} files!'.format(Filecount))