import numpy as np
data = np.loadtxt('Benign 2.txt', dtype='str', delimiter='\n')

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

# determine the unique elements in the sequence
uniqueSys = set(seq)

bagSize = 4
bag = []
SeqMap = {}
for i in range(len(seq)):
    if i < len(seq) - bagSize:
        bag = seq[i:i+bagSize]
        bagStr = ' '.join(bag)
        if bagStr not in SeqMap:
            # determining the frequency of each element of uniqueSys in the bag
            freqMap = {}
            for sys in uniqueSys:
                freqMap[sys] = bag.count(sys)
            SeqMap[bagStr] = freqMap
        else:
            continue

print(SeqMap)

data = np.loadtxt('Malicious 3.txt', dtype='str', delimiter='\n')

# print(data)

newDataTest = []
for i in range(len(data)):
    newDataTest.append(data[i].split(' '))
# print(newData)

seqTest = []
for i in range(len(newDataTest)):
    for j in range(len(newDataTest[i])):
        if newDataTest[i][j] == '<' or newDataTest[i][j] == '>':
            seqTest.append(newDataTest[i][j+1])

# determine the unique elements in the sequence
uniqueSysTest = set(seqTest)


bag = []
SeqMapTest = {}
for i in range(len(seqTest)):
    if i < len(seqTest) - bagSize:
        bag = seqTest[i:i+bagSize]
        bagStr = ' '.join(bag)
        if bagStr not in SeqMapTest:
            # determining the frequency of each element of uniqueSys in the bag
            freqMap = {}
            for sys in uniqueSys:
                freqMap[sys] = bag.count(sys)
            SeqMapTest[bagStr] = freqMap
        else:
            continue

print(SeqMapTest)

matchCount=0
for bag in SeqMapTest:
    if bag in SeqMap:
        matchCount+=1

print(matchCount)
print(len(SeqMapTest) - matchCount)