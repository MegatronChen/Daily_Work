__author__ = 'Megatron_chen'

import os
from tkinter.filedialog import askdirectory


QueryDir = askdirectory(title='Choose the Query directory')
Results = os.listdir(QueryDir)

with open(r'C:\Users\Megatron_chen\Desktop\FileList.txt','w') as f:
    for EachFile in Results:
        f.write(EachFile +'\n')