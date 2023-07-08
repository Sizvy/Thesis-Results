import numpy as np
import os
import math

SourceFolder = 'E:\study materials\Everything of 4-1\All works about thesis\week 15\Freq Accuracy\Benign Text Versions\\'

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


SourceFolder = 'E:\study materials\Everything of 4-1\All works about thesis\week 15\Freq Accuracy\Malicious4 Text Versions\\'
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
            Alldata_mal[i][j][0] = Alldata_mal[i][j][0].replace('k', '')
            temp = float(Alldata_mal[i][j][0]) * 1000
            Alldata_mal[i][j][0] = str(temp)
        if 'K' in Alldata_mal[i][j][0]:
            Alldata_mal[i][j][0] = Alldata_mal[i][j][0].replace('K', '')
            temp = float(Alldata_mal[i][j][0]) * 1000
            Alldata_mal[i][j][0] = str(temp)
        if 'd' in Alldata_mal[i][j][0]:
            Alldata_mal[i][j][0] = Alldata_mal[i][j][0].replace('d', '')

MaliciousSyscallWithFreq = {}
for i in range(int(trainPercentage*len(Alldata_mal))):
    AttackIdentifier = {}
    for j in range(len(Alldata_mal[i])):
        if Alldata_mal[i][j][3] in MaliciousSyscallWithFreq:
            MaliciousSyscallWithFreq[Alldata_mal[i][j][3]] += float(Alldata_mal[i][j][0])
        else:
            MaliciousSyscallWithFreq[Alldata_mal[i][j][3]] = float(Alldata_mal[i][j][0])

for key, value in MaliciousSyscallWithFreq.items():
    MaliciousSyscallWithFreq[key] = value/len(Alldata_mal)

print(MaliciousSyscallWithFreq)

# Percentage change in frequency
RateChange = {}
for key, value in MaliciousSyscallWithFreq.items():
    if key in BenignSyscallWithFreq:
        RateChange[key] = (value - BenignSyscallWithFreq[key])/BenignSyscallWithFreq[key]


RateChangeTotal = sorted(RateChange.items(), key=lambda x: x[1], reverse=True)
RateChangeTotal = dict(RateChangeTotal)
# print(RateChangeTotal)

# take only those who has more than 100% change
RateChangeTotal = {k: v for k, v in RateChangeTotal.items() if v > 1}
print(RateChangeTotal)

ChosenSyscall = {}
Threshold = {}
for key, value in RateChangeTotal.items():
    ChosenSyscall[key] = MaliciousSyscallWithFreq[key]
    Threshold[key] = float((BenignSyscallWithFreq[key]+ChosenSyscall[key])/2)
# print(ChosenSyscall)
print(Threshold)
MalCount=0
for i in range(math.floor(trainPercentage*len(Alldata_mal)), len(Alldata_mal)):
    AttackIdentifier = {}
    for j in range(len(Alldata_mal[i])):
        if Alldata_mal[i][j][3] in Threshold: 
            if float(Alldata_mal[i][j][0]) > Threshold[Alldata_mal[i][j][3]]:
                AttackIdentifier[Alldata_mal[i][j][3]] = 1
            else:
                AttackIdentifier[Alldata_mal[i][j][3]] = 0
    if sum(AttackIdentifier.values()) / len(AttackIdentifier) >= 0.82:
        MalCount += 1
testSize = len(Alldata_mal) - math.floor(trainPercentage*len(Alldata_mal))
print('Attack Detected: ', (MalCount/testSize)*100, '%')