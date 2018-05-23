__author__ = 'Megatron_chen'

import os
from tkinter.messagebox import *
from tkinter.filedialog import askdirectory


QueryDir = askdirectory(title='Choose the Query directory')
if QueryDir:
    QureyResults = os.listdir(QueryDir)

    TargetDir = askdirectory(title='Choose the target directory to generate the result file')

    if TargetDir:
        with open(os.path.join(TargetDir,'FileList.txt'),'w') as f:
            for EachFile in QureyResults:
                f.write(EachFile +'\n')

        Info = showinfo('Process Report','Congratulations! The file names have been listed in the txt! ')

    else:
        warn = showwarning('DirLost','the Result dir has not been specified!')

else:
    warn = showwarning('DirLost','the Query dir has not been specified!')





