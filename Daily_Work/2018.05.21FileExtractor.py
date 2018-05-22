__author__ = 'Megatron_chen'
print('\n')

'''
From a top directory, extract all files of a specified extension name(or severals in a tuple)
from the top directory and all its subdictionary to a target directory by copying all the files
'''


import os
import os.path
import shutil
import tkinter
from tkinter.filedialog import askdirectory


# TopDir = askdirectory(title='Choose the Top directory')
# TargetDir = askdirectory(title='Choose the Target directory')
# Target_FileExtension = ('.jpg','.jpeg')

# TopDir = r'C:\Users\Megatron_chen\Desktop\Top'
# TargetDir = r'C:\Users\Megatron_chen\Desktop\Target'
# Target_FileExtension = ('.txt')

FileNames = []

Filecount = 0
TopDir_Tree_Generator = os.walk(TopDir)
for EachPiece in TopDir_Tree_Generator:
    if len(EachPiece[2]):
        for EachFile in EachPiece[2]:
            if EachFile.endswith(Target_FileExtension):
                if EachFile not in FileNames:
                    FileNames.append(EachFile)
                    shutil.copy(os.path.join(EachPiece[0],EachFile),TargetDir)
                else:
                    RepeteIndex = FileNames.count(EachFile)
                    (basename,fileExtension) = os.path.splitext(EachFile)
                    TargetName = basename + '-Repeat-' + str(RepeteIndex) + fileExtension
                    # print(TargetName)
                    # print(os.path.join(TargetDir,TargetName,fileExtension))
                    shutil.copyfile(os.path.join(EachPiece[0],EachFile),os.path.join(TargetDir,TargetName))

                Filecount += 1

print('Extraction Done! Totally {0} files!'.format(Filecount))