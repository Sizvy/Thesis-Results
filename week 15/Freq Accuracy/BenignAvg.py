import numpy as np
import os

SourceFolder = 'E:\study materials\Everything of 4-1\Thesis\week 15\Freq Accuracy\Benign Text Versions\\'

Alldata=[]
# iterate all files from a directory
for file_name in os.listdir(SourceFolder):
    # print(file_name)
    sourceFile = SourceFolder + file_name
    data = np.loadtxt(sourceFile, dtype=str)
    # print(data)
    Alldata.append(data)

# print(Alldata[0][3][3])

BenignSyscallWithFreq = {}
BenignSyscallWithMaxFreq = {}

for i in range(len(Alldata)):
    for j in range(len(Alldata[i])):
        if 'Â©' in Alldata[i][j][0]:
            Alldata[i][j][0] = Alldata[i][j][0].replace('Â©', '')
        if ',' in Alldata[i][j][0]:
            Alldata[i][j][0] = Alldata[i][j][0].replace(',', '.')
        if '$' in Alldata[i][j][0]:
            Alldata[i][j][0] = Alldata[i][j][0].replace('$', '')
        if Alldata[i][j][3] in BenignSyscallWithFreq:
            BenignSyscallWithFreq[Alldata[i][j][3]] += float(Alldata[i][j][0])
            if BenignSyscallWithMaxFreq[Alldata[i][j][3]] < float(Alldata[i][j][0]):
                BenignSyscallWithMaxFreq[Alldata[i][j][3]] = float(Alldata[i][j][0])
        else:
            BenignSyscallWithFreq[Alldata[i][j][3]] = float(Alldata[i][j][0])
            BenignSyscallWithMaxFreq[Alldata[i][j][3]] = float(Alldata[i][j][0])

for key, value in BenignSyscallWithFreq.items():
    BenignSyscallWithFreq[key] = value/len(Alldata)

# print(BenignSyscallWithFreq)
# print(BenignSyscallWithMaxFreq)


SourceFolder = 'E:\study materials\Everything of 4-1\Thesis\week 15\Freq Accuracy\Benign Text Versions(Testing Data)\\'
Alldata_mal=[]
# iterate all files from a directory
for file_name in os.listdir(SourceFolder):
    # print(file_name)
    sourceFile = SourceFolder + file_name
    data = np.loadtxt(sourceFile, dtype=str)
    # print(data)
    Alldata_mal.append(data)

# print(Alldata_mal)

MalCount=0
for i in range(len(Alldata_mal)):
    AttackIdentifier = {}
    for j in range(len(Alldata_mal[i])):
        if 'Â©' in Alldata_mal[i][j][0]:
            Alldata_mal[i][j][0] = Alldata_mal[i][j][0].replace('Â©', '')
        if ',' in Alldata_mal[i][j][0]:
            Alldata_mal[i][j][0] = Alldata_mal[i][j][0].replace(',', '.')
        if '$' in Alldata_mal[i][j][0]:
            Alldata_mal[i][j][0] = Alldata_mal[i][j][0].replace('$', '')
        if 'k' in Alldata_mal[i][j][0]:
            Alldata_mal[i][j][0] = Alldata_mal[i][j][0].replace('k', '000')
            Alldata_mal[i][j][0] = Alldata_mal[i][j][0].replace('.', '')
        if 'K' in Alldata_mal[i][j][0]:
            Alldata_mal[i][j][0] = Alldata_mal[i][j][0].replace('K', '000')
            Alldata_mal[i][j][0] = Alldata_mal[i][j][0].replace('.', '')
        if 'd' in Alldata_mal[i][j][0]:
            Alldata_mal[i][j][0] = Alldata_mal[i][j][0].replace('d', '')
        if float(Alldata_mal[i][j][0]) > 10: 
            if Alldata_mal[i][j][3] in BenignSyscallWithMaxFreq:
                if BenignSyscallWithMaxFreq[Alldata_mal[i][j][3]] < float(Alldata_mal[i][j][0]):
                    AttackIdentifier[Alldata_mal[i][j][3]] = 1
                    # print('Malicious1: ', Alldata_mal[i][j][3], ' ', Alldata_mal[i][j][0], 'crossed the threshold')
                else:
                    AttackIdentifier[Alldata_mal[i][j][3]] = 0
                    # print('Benign: ', Alldata_mal[i][j][3], ' ', Alldata_mal[i][j][0], 'is within the threshold')
            else:
                AttackIdentifier[Alldata_mal[i][j][3]] = 1
                # print('Malicious1: ', Alldata_mal[i][j][3], ' ', Alldata_mal[i][j][0], 'seems to be a new syscall')
    # print(AttackIdentifier)
    # print(sum(AttackIdentifier.values()) / len(AttackIdentifier))
    if sum(AttackIdentifier.values()) >= 1:
        # print('Malicious1: ',i, ' is an attack')
        MalCount += 1

# print('Malicious1: ', MalCount, ' attacks found')
# print('Attack Detected: ', MalCount/len(Alldata_mal)*100, '%')
print('Benign Detected: ', (len(Alldata_mal) - MalCount)/len(Alldata_mal)*100, '%')