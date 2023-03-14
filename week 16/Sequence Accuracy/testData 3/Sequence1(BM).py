import numpy as np
count = 0
Total = 0
uniqueSysWithWeight = {'mprotect': 3,'setsockopt': 6, 'epoll_wait': 0, 'futex': 6, 'close': 3, 'pwrite': 3, 'sched_yield': 3, 'gettid': 0, 'poll': 3, 'fsync': 0, 'getpid': 4, 'shutdown': 6, 'munmap': 3, 'recvfrom': 6, 'io_submit': 0, 'ppoll': 0, 'sendto': 6, 'getpeername': 6, 'nanosleep': 3, 'io_getevents': 0, 'fdatasync': 0, 'sched_getaffinity': 0, 'getrusage': 0, 'mmap': 3, 'switch': 3, 'write': 3, 'accept': 6}
for m in range(1, 21):
    data = np.loadtxt('benign_'+str(m)+'.txt', dtype='str', delimiter='\n')

    # print(data)

    newData = []
    for i in range(len(data)):
        newData.append(data[i].split(' '))
    # print(newData)

    seq = []
    for i in range(len(newData)):
        for j in range(len(newData[i])):
            if newData[i][j] == '<' or newData[i][j] == '>':
                # print(newData[i][j+1], m, i, j)
                seq.append(newData[i][j+1])

        # determine the unique elements in the sequence
    uniqueSys = set(seq)
    uniqueSys = uniqueSys - {'<unknown>', '', 'sysdigevent'}

    for n in range(1, 21):
        
        Total += 1
        # print(uniqueSys)

        data = np.loadtxt('malicious_'+str(n)+'.txt', dtype='str', delimiter='\n')

        # print(data)

        newDataTest = []
        for i in range(len(data)):
            newDataTest.append(data[i].split(' '))
        # print(newData)

        seqTest = []
        for i in range(len(newDataTest)):
            for j in range(len(newDataTest[i])):
                if newDataTest[i][j] == '<' or newDataTest[i][j] == '>':
                    # print(newDataTest[i][j+1], n, i, j)
                    seqTest.append(newDataTest[i][j+1])

        # determine the unique elements in the sequence
        uniqueSysTest = set(seqTest)
        uniqueSysTest = uniqueSysTest - {'<unknown>', '','sysdigevent'}
        # print(uniqueSysTest)

        if(len(uniqueSys) > len(uniqueSysTest)):
            uniqueSys = uniqueSysTest
        else:
            uniqueSysTest = uniqueSys

        bagSize = 8
        bag = []
        SeqMap = {}
        SysCallFreqMap = {}
        for i in range(len(seq)):
            if i < len(seq) - bagSize:
                bag = seq[i:i+bagSize]
                bagStr = ' '.join(bag)
                if bagStr not in SeqMap:
                    # determining the frequency of each element of uniqueSys in the bag
                    SysCallFreqMap[bagStr] = 1
                    freqMap = {}
                    for sys in uniqueSys:
                        freqMap[sys] = bag.count(sys)
                    SeqMap[bagStr] = freqMap
                else:
                    SysCallFreqMap[bagStr] += 1
                    continue

        # print(SeqMap)



        bag = []
        SeqMapTest = {}
        SysCallFreqMapTest = {}
        for i in range(len(seqTest)):
            if i < len(seqTest) - bagSize:
                bag = seqTest[i:i+bagSize]
                bagStr = ' '.join(bag)
                if bagStr not in SeqMapTest:
                    # determining the frequency of each element of uniqueSys in the bag
                    SysCallFreqMapTest[bagStr] = 1
                    freqMap = {}
                    for sys in uniqueSysTest:
                        freqMap[sys] = bag.count(sys)
                    SeqMapTest[bagStr] = freqMap
                else:
                    SysCallFreqMapTest[bagStr] += 1
                    continue

        # print(SeqMap)
        # print(SeqMapTest)

        # print(uniqueSys)

        matchCount=0
        misMatchCount=0
        for bag in SeqMapTest:
            if SeqMapTest[bag] in SeqMap.values():
                for elements in SeqMapTest[bag]:
                    matchCount += (uniqueSysWithWeight[elements] * SeqMapTest[bag][elements]) 
                # matchCount+=1
            else: 
                misMatchCount += len(uniqueSys)


        # print(len(SeqMap))
        # print(matchCount)
        # print(len(SeqMap) - matchCount)
        # print('Match ratio: ', matchCount/len(SeqMap))
        # with open('result.txt', 'a') as f:
        #     f.write('Match ratio: '+str(m)+' '+str(n)+' '+str(matchCount/len(SeqMap))+'\n')
        if matchCount/(matchCount+misMatchCount) > 0.77:
            count += 1
        # print(matchCount)
        # print(misMatchCount+matchCount)
print(count)
print(Total)
print((Total-count)/Total)