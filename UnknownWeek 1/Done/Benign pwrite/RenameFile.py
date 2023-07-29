import os
# rename every file in this directory
sourceFolder = r'E:\study materials\\Everything of 4-1\\All works about thesis\\UnknownWeek 1\\Done\\Benign io_submit\\'
i=1
for file_name in os.listdir(sourceFolder):
    print(file_name)
    sourceFile = sourceFolder + file_name
    os.rename(sourceFile, 'benign_'+'iosubmit_'+file_name)
    i = i+1