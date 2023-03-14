import numpy as np
data = np.loadtxt('benign 1.txt', dtype='str', delimiter='\n')

# print(data)

newData = []
for i in range(len(data)):
    newData.append(data[i].split(' '))
# print(newData)

seq = []
for i in range(len(newData)):
    for j in range(len(newData[i])):
        if newData[i][j] == '<' or newData[i][j] == '>':
            seq.append(newData[i][j+1])

# print(seq)

bagSize = 10
bag = []

seqFreqMap = {}
for i in range(len(seq)):
    if i < len(seq) - bagSize:
        bag = seq[i:i+bagSize]
        bag = ' '.join(bag)
        if bag not in seqFreqMap:
            seqFreqMap[bag] = 1
        else:
            seqFreqMap[bag] += 1

# print(seqFreqMap)
print(len(seqFreqMap))


MaliciousData = np.loadtxt('benign 2.txt', dtype='str', delimiter='\n')

# print(data)

newMaliciousData = []
for i in range(len(MaliciousData)):
    newMaliciousData.append(MaliciousData[i].split(' '))
# print(newData)

Malseq = []
for i in range(len(newMaliciousData)):
    for j in range(len(newMaliciousData[i])):
        if newMaliciousData[i][j] == '<' or newMaliciousData[i][j] == '>':
            Malseq.append(newMaliciousData[i][j+1])

# print(seq)
MalseqFreqMap = {}
for i in range(len(Malseq)):
    if i < len(Malseq) - bagSize:
        bag = Malseq[i:i+bagSize]
        bag = ' '.join(bag)
        if bag not in MalseqFreqMap:
            MalseqFreqMap[bag] = 1
        else:
            MalseqFreqMap[bag] += 1

# print(MalseqFreqMap)
print(len(MalseqFreqMap))


matchCount=0
# Matching two dictionaries:
for sequence in MalseqFreqMap:
    if sequence in seqFreqMap:
        matchCount += 1

print(matchCount)
print(len(MalseqFreqMap) - matchCount)
