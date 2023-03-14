import numpy as np
import matplotlib.pyplot as plt
import os

for field in range(1,7):
# field=2
    tp=[]
    fp=[]
    fn=[]
    tn=[]
    Accuracy=[]
    Precision=[]
    Recall=[]
    F1_Score=[]

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


    MaliciousSyscallWithFreq = {}
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
            if Alldata_mal[i][j][3] in MaliciousSyscallWithFreq:
                MaliciousSyscallWithFreq[Alldata_mal[i][j][3]] += float(Alldata_mal[i][j][0])
            else:
                MaliciousSyscallWithFreq[Alldata_mal[i][j][3]] = float(Alldata_mal[i][j][0])

    for key, value in MaliciousSyscallWithFreq.items():
        MaliciousSyscallWithFreq[key] = value/len(Alldata_mal)

    # print(MaliciousSyscallWithFreq)

    # Percentage change in frequency
    RateChange = {}
    for key, value in MaliciousSyscallWithFreq.items():
        if key in BenignSyscallWithFreq:
            RateChange[key] = abs(value - BenignSyscallWithFreq[key])/BenignSyscallWithFreq[key]

    # print(RateChange)

    RateChangeTotal = sorted(RateChange.items(), key=lambda x: x[1], reverse=True)



    for n in range(1,18):
        RateChange = RateChangeTotal[:n]
        RateChange = dict(RateChange)
        # print(RateChange)

        MalCount=0
        for i in range(len(Alldata_mal)):
            AttackIdentifier = {}
            for j in range(len(Alldata_mal[i])):
                # print(Alldata_mal[i][j][3])
                if Alldata_mal[i][j][3] in RateChange: 
                    # print(Alldata_mal[i][j][3])
                    if Alldata_mal[i][j][3] in BenignSyscallWithFreq:
                        if BenignSyscallWithMaxFreq[Alldata_mal[i][j][3]] < float(Alldata_mal[i][j][0]):
                            AttackIdentifier[Alldata_mal[i][j][3]] = 1
                            # print('Malicious1: ', Alldata_mal[i][j][3], ' ', Alldata_mal[i][j][0], 'crossed the threshold')
                        else:
                            AttackIdentifier[Alldata_mal[i][j][3]] = 0
                            # print('Benign: ', Alldata_mal[i][j][3], ' ', Alldata_mal[i][j][0], 'is within the threshold')
                    else:
                        AttackIdentifier[Alldata_mal[i][j][3]] = 1
                        # print('Malicious1: ', Alldata_mal[i][j][3], ' ', Alldata_mal[i][j][0], 'seems to be a new syscall')
                # else:
                #     continue
                    # print('Benign: ', Alldata_mal[i][j][3], ' ', Alldata_mal[i][j][0], 'is not in the list')
            if len(AttackIdentifier)>0 and sum(AttackIdentifier.values()) / len(AttackIdentifier) > 0.5:
                MalCount += 1
            
        # print('Benign Detected: ', (len(Alldata_mal) - MalCount)/len(Alldata_mal)*100, '%')
        fp.append(MalCount)
        tn.append(len(Alldata_mal) - MalCount)

    print('Benign Done')
    ############################################################################################################################################################################


    SourceFolder = 'E:\study materials\Everything of 4-1\Thesis\week 15\Freq Accuracy\Malicious'+str(field)+' Text Versions\\'
    Alldata_mal=[]
    # iterate all files from a directory
    for file_name in os.listdir(SourceFolder):
        # print(file_name)
        sourceFile = SourceFolder + file_name
        data = np.loadtxt(sourceFile, dtype=str)
        # print(data)
        Alldata_mal.append(data)

    # print(Alldata_mal)


    MaliciousSyscallWithFreq = {}
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
            if Alldata_mal[i][j][3] in MaliciousSyscallWithFreq:
                MaliciousSyscallWithFreq[Alldata_mal[i][j][3]] += float(Alldata_mal[i][j][0])
            else:
                MaliciousSyscallWithFreq[Alldata_mal[i][j][3]] = float(Alldata_mal[i][j][0])

    for key, value in MaliciousSyscallWithFreq.items():
        MaliciousSyscallWithFreq[key] = value/len(Alldata_mal)

    # print(MaliciousSyscallWithFreq)

    # Percentage change in frequency
    RateChange = {}
    for key, value in MaliciousSyscallWithFreq.items():
        if key in BenignSyscallWithFreq:
            RateChange[key] = (value - BenignSyscallWithFreq[key])/BenignSyscallWithFreq[key]

    # print(RateChange)

    RateChangeTotal = sorted(RateChange.items(), key=lambda x: x[1], reverse=True)
    # print(RateChange)


    for n in range(1,18):
        RateChange = RateChangeTotal[:n]
        RateChange = dict(RateChange)
        # print(RateChange)

        MalCount=0
        for i in range(len(Alldata_mal)):
            AttackIdentifier = {}
            for j in range(len(Alldata_mal[i])):
                if Alldata_mal[i][j][3] in RateChange: 
                    # print(n, Alldata_mal[i][j][3], i)
                    if Alldata_mal[i][j][3] in BenignSyscallWithFreq:
                        # print('here', Alldata_mal[i][j][3], i, n)
                        if BenignSyscallWithMaxFreq[Alldata_mal[i][j][3]] < float(Alldata_mal[i][j][0]):
                            AttackIdentifier[Alldata_mal[i][j][3]] = 1
                            # print('Malicious1: ', Alldata_mal[i][j][3], ' ', Alldata_mal[i][j][0], 'crossed the threshold')
                        else:
                            AttackIdentifier[Alldata_mal[i][j][3]] = 0
                            # print('Benign: ', Alldata_mal[i][j][3], ' ', Alldata_mal[i][j][0], 'is within the threshold')
                    else:
                        AttackIdentifier[Alldata_mal[i][j][3]] = 1
                        # print('Malicious1: ', Alldata_mal[i][j][3], ' ', Alldata_mal[i][j][0], 'seems to be a new syscall')
            
            if len(AttackIdentifier)>0 and sum(AttackIdentifier.values()) / len(AttackIdentifier) > 0.5:
                MalCount += 1
                # print('Attack Detected: ', AttackIdentifier)
        # print('Attack Detected: ', (MalCount)/len(Alldata_mal)*100, '%')
        tp.append(MalCount)
        fn.append(len(Alldata_mal) - MalCount)

    print('Malicious Done')
    X=[]
    for i in range(1,18):
        print(RateChangeTotal[i-1][0])
        X.append("S"+str(i))    
        Accuracy.append((tp[i-1]+tn[i-1])/(tp[i-1]+tn[i-1]+fp[i-1]+fn[i-1]))
        Precision.append(tp[i-1]/(tp[i-1]+fp[i-1]))
        Recall.append(tp[i-1]/(tp[i-1]+fn[i-1]))
        F1_Score.append(2*Precision[i-1]*Recall[i-1]/(Precision[i-1]+Recall[i-1]))

    plt.plot(X, Accuracy, label = "Accuracy", linestyle='-.')
    plt.plot(X, Precision, label = "Precision", linestyle='--')
    plt.plot(X, Recall, label = "Recall",linestyle=':')
    plt.plot(X, F1_Score, label = "F1 Score", linestyle='-')
    plt.xlabel('Set of Syscalls', fontsize=12)
    plt.ylabel('Metrics value', fontsize=12)
    plt.title('Impact of Each System call with Modified field='+str(field))
    plt.legend(fontsize=12)
    plt.show()

