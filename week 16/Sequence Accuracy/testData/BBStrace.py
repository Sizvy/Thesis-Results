import numpy as np
import matplotlib.pyplot as plt

X=[]
Y1=[]
Y2=[]
for bagSize in range(2, 20):
    X.append(bagSize)
    benignTrue=0
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
                benignTrue += 1
                # print("Benign")

    # print("Correct Match(True Positive): ", benignTrue)
    # print("Overall Count: ", Overallcount)
    # print("Benign Detection Accuracy: ", (benignTrue)/Overallcount)
    Y1.append((benignTrue)/Overallcount)

for bagSize in range(2, 20):
    # X.append(bagSize)
    benignTrue=0
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
                benignTrue += 1
                # print("Benign")

    # print("Wrong Match: ", benignTrue)
    # print("Overall Count: ", Overallcount)
    # print("Malicious Detection Accuracy: ", (Overallcount - benignTrue)/Overallcount)
    Y2.append((Overallcount - benignTrue)/Overallcount)

# print(Y)
plt.plot(X,Y1, label='Benign Detection Accuracy', linestyle='-.')
plt.plot(X,Y2, label='Malicious Detection Accuracy', linestyle='--')
plt.xlabel('Bag Size')
plt.ylabel('Accuracy')
plt.title('Detection Accuracy vs Bag Size')
plt.legend()
plt.show()