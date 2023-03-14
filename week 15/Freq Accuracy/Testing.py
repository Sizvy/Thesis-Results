import numpy as np
import os

SourceFolder = 'E:\study materials\Everything of 4-1\Thesis\week 15\Freq Accuracy\Malicious1 Text Versions\\'
Alldata_mal=[]
# iterate all files from a directory
for file_name in os.listdir(SourceFolder):
    # print(file_name)
    sourceFile = SourceFolder + file_name
    data = np.loadtxt(sourceFile, dtype=str)
    # print(data)
    Alldata_mal.append(data)

# print(Alldata_mal)
trainPercentage = 0.7

MaliciousSyscallWithFreq = {}
for i in range(int(trainPercentage*len(Alldata_mal))):
    AttackIdentifier = {}
    if i == 58:
            print(i, Alldata_mal[i])
    for j in range(len(Alldata_mal[i])):
        # if Alldata_mal[i][j][3] == 'nanosleep':
        #     if float(Alldata_mal[i][j][0]) > 50:
        #         print(i , j, Alldata_mal[i][j][0], Alldata_mal[i][j][3])
        if 'Â©' in Alldata_mal[i][j][0]:
            Alldata_mal[i][j][0] = Alldata_mal[i][j][0].replace('Â©', '')
        if ',' in Alldata_mal[i][j][0]:
            Alldata_mal[i][j][0] = Alldata_mal[i][j][0].replace(',', '.')
        if '$' in Alldata_mal[i][j][0]:
            Alldata_mal[i][j][0] = Alldata_mal[i][j][0].replace('$', '')
        if 'k' in Alldata_mal[i][j][0]:
            Alldata_mal[i][j][0] = Alldata_mal[i][j][0].replace('k', '')
            temp = float(Alldata_mal[i][j][0]) * 1000
            Alldata_mal[i][j][0] = str(temp)
        if 'K' in Alldata_mal[i][j][0]:
            Alldata_mal[i][j][0] = Alldata_mal[i][j][0].replace('K', '')
            temp = float(Alldata_mal[i][j][0]) * 1000
            Alldata_mal[i][j][0] = str(temp)
        if 'd' in Alldata_mal[i][j][0]:
            Alldata_mal[i][j][0] = Alldata_mal[i][j][0].replace('d', '')
        if Alldata_mal[i][j][3] in MaliciousSyscallWithFreq:
            MaliciousSyscallWithFreq[Alldata_mal[i][j][3]] += float(Alldata_mal[i][j][0])
        else:
            MaliciousSyscallWithFreq[Alldata_mal[i][j][3]] = float(Alldata_mal[i][j][0])

for key, value in MaliciousSyscallWithFreq.items():
    MaliciousSyscallWithFreq[key] = value/len(Alldata_mal)

print(MaliciousSyscallWithFreq)
