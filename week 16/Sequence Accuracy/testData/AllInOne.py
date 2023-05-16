import numpy as np
import matplotlib.pyplot as plt
X=[]
AccuracyY=[]
PrecisionY=[]
RecallY=[]
F1ScoreY=[]
for bagSize in range(2, 20):
    X.append(bagSize)
    trueNegative=0
    Overallcount=0
    for m in range(1, 101):
        data = np.loadtxt('benign_'+str(m)+'.log', dtype='str', delimiter='\n')

        # print(data)

        newData = []
        for i in range(0,len(data)):
            newData.append(data[i].split(' '))
        #print(newData)

        seq = []
        for i in range(0,len(newData)):
            value = newData[i][0].split('(')
            seq.append(value[0])

        # print(seq)

        bag = []

        seqFreqMap = {}
        for i in range(0,len(seq)):
            if i < len(seq) - bagSize:
                bag = seq[i:i+bagSize]
                bag = ' '.join(bag)
                if bag not in seqFreqMap:
                    seqFreqMap[bag] = 1
                else:
                    seqFreqMap[bag] += 1

        for n in range(m+1,101):
            Overallcount+=1
            

            # print(seqFreqMap)
            # print(len(seqFreqMap))


            MaliciousData = np.loadtxt('benign_'+str(n)+'.log', dtype='str', delimiter='\n')

            # print(data)

            newMaliciousData = []
            for i in range(0,len(MaliciousData)):
                newMaliciousData.append(MaliciousData[i].split(' '))
            # print(newData)

            Malseq = []
            for i in range(0,len(newMaliciousData)):
                value = newMaliciousData[i][0].split('(')
                Malseq.append(value[0])
            # print("LOL")
            # print(Malseq)
            MalseqFreqMap = {}
            for i in range(0,len(Malseq)):
                if i < len(Malseq) - bagSize:
                    bag = Malseq[i:i+bagSize]
                    bag = ' '.join(bag)
                    if bag not in MalseqFreqMap:
                        MalseqFreqMap[bag] = 1
                    else:
                        MalseqFreqMap[bag] += 1

            # print(MalseqFreqMap)
            # print(len(MalseqFreqMap))


            matchCount=0
            # Matching two dictionaries:
            for sequence in MalseqFreqMap:
                if sequence in seqFreqMap and abs(MalseqFreqMap[sequence] - seqFreqMap[sequence]) <= 4:
                    matchCount += 1

            # print("Match: ", matchCount)
            # print("Mismatch: ", len(MalseqFreqMap) - matchCount)

            if matchCount / len(MalseqFreqMap) >= 0.8:
                trueNegative += 1
                # print("Benign")

    # print("Correct Match(True Positive): ", trueNegative)
    # print("Overall Count: ", Overallcount)
    # print("Benign Detection Accuracy: ", (trueNegative)/Overallcount)
    # Y.append((benignTrue)/Overallcount)

    falsePositive = Overallcount - trueNegative
    Overallcount = 0
    falseNegative = 0

    for m in range(1, 101):
        data = np.loadtxt('benign_'+str(m)+'.log', dtype='str', delimiter='\n')

        # print(data)

        newData = []
        for i in range(0,len(data)):
            newData.append(data[i].split(' '))
        #print(newData)

        seq = []
        for i in range(0,len(newData)):
            value = newData[i][0].split('(')
            seq.append(value[0])

        # print(seq)

        # bagSize = 20
        bag = []

        seqFreqMap = {}
        for i in range(0,len(seq)):
            if i < len(seq) - bagSize:
                bag = seq[i:i+bagSize]
                bag = ' '.join(bag)
                if bag not in seqFreqMap:
                    seqFreqMap[bag] = 1
                else:
                    seqFreqMap[bag] += 1

        for n in range(1,101):
            Overallcount+=1
            

            # print(seqFreqMap)
            # print(len(seqFreqMap))


            MaliciousData = np.loadtxt('malicious_'+str(n)+'.log', dtype='str', delimiter='\n')

            # print(data)

            newMaliciousData = []
            for i in range(0,len(MaliciousData)):
                newMaliciousData.append(MaliciousData[i].split(' '))
            # print(newData)

            Malseq = []
            for i in range(0,len(newMaliciousData)):
                value = newMaliciousData[i][0].split('(')
                Malseq.append(value[0])
            # print("LOL")
            # print(Malseq)
            MalseqFreqMap = {}
            for i in range(0,len(Malseq)):
                if i < len(Malseq) - bagSize:
                    bag = Malseq[i:i+bagSize]
                    bag = ' '.join(bag)
                    if bag not in MalseqFreqMap:
                        MalseqFreqMap[bag] = 1
                    else:
                        MalseqFreqMap[bag] += 1

            # print(MalseqFreqMap)
            # print(len(MalseqFreqMap))


            matchCount=0
            # Matching two dictionaries:
            for sequence in MalseqFreqMap:
                if sequence in seqFreqMap and abs(MalseqFreqMap[sequence] - seqFreqMap[sequence]) <= 4:
                    matchCount += 1

            # print("Match: ", matchCount)
            # print("Mismatch: ", len(MalseqFreqMap) - matchCount)

            if matchCount / len(MalseqFreqMap) >= 0.8:
                falseNegative += 1
                # print("Benign")

    # print("Wrong Match: ", truePositive)
    # print("Overall Count: ", Overallcount)
    # print("Malicious Detection Accuracy: ", (Overallcount - truePositive)/Overallcount)

    truePositive = Overallcount - falseNegative

    # print("Bag Size: ", bagSize)
    # print("True Positive: ", trueNegative)
    # print("False Positive: ", falsePositive)
    # print("True Negative: ", truePositive)
    # print("False Negative: ", falseNegative)

    AccuracyY.append((trueNegative + truePositive)/(trueNegative + truePositive + falseNegative + falsePositive))
    PrecisionY.append(truePositive/(truePositive + falsePositive))
    RecallY.append(truePositive/(truePositive + falseNegative))
    F1ScoreY.append(2 * (PrecisionY[bagSize-3] * RecallY[bagSize-3]) / (PrecisionY[bagSize-3] + RecallY[bagSize-3]))


plt.plot(X, AccuracyY, label = "Accuracy", linestyle='-.')
plt.plot(X, PrecisionY, label = "Precision", linestyle='-')
plt.plot(X, RecallY, label = "Recall", linestyle=':')
plt.plot(X, F1ScoreY, label = "F1 Score", linestyle='--')
plt.xlabel('Bag Size', fontsize = 15)
plt.ylabel('Metric Value', fontsize = 15)
plt.title('Bag Size vs Metric Values', fontsize = 12)
plt.legend(fontsize = 12)
plt.show()

