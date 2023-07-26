import os
# rename every file in this directory
sourceFolder = r'E:\study materials\\Everything of 4-1\\All works about thesis\\UnknownWeek 1\\Done\\Benign pwrite\\'
for file_name in os.listdir(sourceFolder):
    print(file_name)
    sourceFile = sourceFolder + file_name
    os.rename(sourceFile, 'benign_' + 'pwrite_' + file_name)