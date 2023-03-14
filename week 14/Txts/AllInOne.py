import numpy as np
import matplotlib.pyplot as plt
malicious_list_of_sysCall_with_frequency_1 = {}
malicious_list_of_sysCall_with_frequency_2 = {}
malicious_list_of_sysCall_with_frequency_3 = {}
malicious_list_of_sysCall_with_frequency_4 = {}
malicious_list_of_sysCall_with_frequency_5 = {}
malicious_list_of_sysCall_with_frequency_6 = {}
benign_list_of_sysCall_with_frequency = {}

SysCall_name = []
mal_SysCall_frequency = []
ben_SysCall_frequency = []

for j in range(1, 6):
    # data = []
    # with open('benign '+str(j)+'.txt', 'r') as f:
    #     for row in f.read().strip().split("\n")[3:]:
    #         data.append(row.split(" "))
    data = np.loadtxt('benign '+str(j)+'.txt', dtype=str)
    # print(len(data))
    for i in range(len(data)):
        if data[i][3] in benign_list_of_sysCall_with_frequency:
            benign_list_of_sysCall_with_frequency[data[i][3]] += float(data[i][0])
        else:
            benign_list_of_sysCall_with_frequency[data[i][3]] = float(data[i][0])
for i in range(len(data)):
    benign_list_of_sysCall_with_frequency[data[i][3]] = benign_list_of_sysCall_with_frequency[data[i][3]]/5

for j in range(1, 6):
    data = np.loadtxt('mal1_'+str(j)+'.txt', dtype=str)
    # print(data)
    data[0][0] = float(data[0][0].replace('K', ''))*1000.0
    for i in range(len(data)):
        
        if data[i][3] in malicious_list_of_sysCall_with_frequency_1:
            malicious_list_of_sysCall_with_frequency_1[data[i][3]] += float(data[i][0])
        else:
            malicious_list_of_sysCall_with_frequency_1[data[i][3]] = float(data[i][0])
for i in range(len(data)):
    malicious_list_of_sysCall_with_frequency_1[data[i][3]] = malicious_list_of_sysCall_with_frequency_1[data[i][3]]/5


for j in range(1, 6):
    data = np.loadtxt('mal2_'+str(j)+'.txt', dtype=str)
    # print(data)
    data[0][0] = float(data[0][0].replace('K', ''))*1000.0
    for i in range(len(data)):
        
        if data[i][3] in malicious_list_of_sysCall_with_frequency_2:
            malicious_list_of_sysCall_with_frequency_2[data[i][3]] += float(data[i][0])
        else:
            malicious_list_of_sysCall_with_frequency_2[data[i][3]] = float(data[i][0])
for i in range(len(data)):
    malicious_list_of_sysCall_with_frequency_2[data[i][3]] = malicious_list_of_sysCall_with_frequency_2[data[i][3]]/5

for j in range(1, 6):
    data = np.loadtxt('mal3_'+str(j)+'.txt', dtype=str)
    # print(data)
    data[0][0] = float(data[0][0].replace('K', ''))*1000.0
    for i in range(len(data)):
        if data[i][3] in malicious_list_of_sysCall_with_frequency_3:
            malicious_list_of_sysCall_with_frequency_3[data[i][3]] += float(data[i][0])
        else:
            malicious_list_of_sysCall_with_frequency_3[data[i][3]] = float(data[i][0])
for i in range(len(data)):
    malicious_list_of_sysCall_with_frequency_3[data[i][3]] = malicious_list_of_sysCall_with_frequency_3[data[i][3]]/5

for j in range(1, 6):
    data = np.loadtxt('mal4_'+str(j)+'.txt', dtype=str)
    # print(data)
    data[0][0] = float(data[0][0].replace('K', ''))*1000.0
    for i in range(len(data)):
        if data[i][3] in malicious_list_of_sysCall_with_frequency_4:
            malicious_list_of_sysCall_with_frequency_4[data[i][3]] += float(data[i][0])
        else:
            malicious_list_of_sysCall_with_frequency_4[data[i][3]] = float(data[i][0])
for i in range(len(data)):
    malicious_list_of_sysCall_with_frequency_4[data[i][3]] = malicious_list_of_sysCall_with_frequency_4[data[i][3]]/5

for j in range(1, 6):
    data = np.loadtxt('mal5_'+str(j)+'.txt', dtype=str)
    # print(data)
    data[0][0] = float(data[0][0].replace('K', ''))*1000.0
    for i in range(len(data)):
        if data[i][3] in malicious_list_of_sysCall_with_frequency_5:
            malicious_list_of_sysCall_with_frequency_5[data[i][3]] += float(data[i][0])
        else:
            malicious_list_of_sysCall_with_frequency_5[data[i][3]] = float(data[i][0])
for i in range(len(data)):
    malicious_list_of_sysCall_with_frequency_5[data[i][3]] = malicious_list_of_sysCall_with_frequency_5[data[i][3]]/5

for j in range(1, 6):
    data = np.loadtxt('mal6_'+str(j)+'.txt', dtype=str)
    # print(data)
    data[0][0] = float(data[0][0].replace('K', ''))*1000.0
    for i in range(len(data)):
        if data[i][3] in malicious_list_of_sysCall_with_frequency_6:
            malicious_list_of_sysCall_with_frequency_6[data[i][3]] += float(data[i][0])
        else:
            malicious_list_of_sysCall_with_frequency_6[data[i][3]] = float(data[i][0])
for i in range(len(data)):
    malicious_list_of_sysCall_with_frequency_6[data[i][3]] = malicious_list_of_sysCall_with_frequency_6[data[i][3]]/5

# print(malicious_list_of_sysCall_with_frequency_1)
# print(malicious_list_of_sysCall_with_frequency_2)
# print(malicious_list_of_sysCall_with_frequency_3)
# print(malicious_list_of_sysCall_with_frequency_4)
# print(malicious_list_of_sysCall_with_frequency_5)
# print(malicious_list_of_sysCall_with_frequency_6)
# print(benign_list_of_sysCall_with_frequency)

X = np.arange(0,7)
# Y = [benign_list_of_sysCall_with_frequency['futex'], malicious_list_of_sysCall_with_frequency_1['futex'], malicious_list_of_sysCall_with_frequency_2['futex'], malicious_list_of_sysCall_with_frequency_3['futex'], malicious_list_of_sysCall_with_frequency_4['futex'], malicious_list_of_sysCall_with_frequency_5['futex'], malicious_list_of_sysCall_with_frequency_6['futex']]
# plt.plot(X, Y, label='futex')
# plt.xlabel('Number of Manipulated fields')
# plt.ylabel('Frequency of futex')
# plt.title('Frequency of futex with number of manipulated fields')
# plt.legend()
# plt.show()

Y = [benign_list_of_sysCall_with_frequency['write'], malicious_list_of_sysCall_with_frequency_1['write'], malicious_list_of_sysCall_with_frequency_2['write'], malicious_list_of_sysCall_with_frequency_3['write'], malicious_list_of_sysCall_with_frequency_4['write'], malicious_list_of_sysCall_with_frequency_5['write'], malicious_list_of_sysCall_with_frequency_6['write']]
plt.plot(X, Y, label='write')
Y = [benign_list_of_sysCall_with_frequency['sendto'], malicious_list_of_sysCall_with_frequency_1['sendto'], malicious_list_of_sysCall_with_frequency_2['sendto'], malicious_list_of_sysCall_with_frequency_3['sendto'], malicious_list_of_sysCall_with_frequency_4['sendto'], malicious_list_of_sysCall_with_frequency_5['sendto'], malicious_list_of_sysCall_with_frequency_6['sendto']]
plt.plot(X, Y, label='sendto')
Y = [benign_list_of_sysCall_with_frequency['recvfrom'], malicious_list_of_sysCall_with_frequency_1['recvfrom'], malicious_list_of_sysCall_with_frequency_2['recvfrom'], malicious_list_of_sysCall_with_frequency_3['recvfrom'], malicious_list_of_sysCall_with_frequency_4['recvfrom'], malicious_list_of_sysCall_with_frequency_5['recvfrom'], malicious_list_of_sysCall_with_frequency_6['recvfrom']]
plt.plot(X, Y, label='recvfrom')
Y = [benign_list_of_sysCall_with_frequency['pwrite'], malicious_list_of_sysCall_with_frequency_1['pwrite'], malicious_list_of_sysCall_with_frequency_2['pwrite'], malicious_list_of_sysCall_with_frequency_3['pwrite'], malicious_list_of_sysCall_with_frequency_4['pwrite'], malicious_list_of_sysCall_with_frequency_5['pwrite'], malicious_list_of_sysCall_with_frequency_6['pwrite']]
plt.plot(X, Y, label='pwrite')
Y = [benign_list_of_sysCall_with_frequency['fsync'], malicious_list_of_sysCall_with_frequency_1['fsync'], malicious_list_of_sysCall_with_frequency_2['fsync'], malicious_list_of_sysCall_with_frequency_3['fsync'], malicious_list_of_sysCall_with_frequency_4['fsync'], malicious_list_of_sysCall_with_frequency_5['fsync'], malicious_list_of_sysCall_with_frequency_6['fsync']]
plt.plot(X, Y, label='fsync')
# Y = [benign_list_of_sysCall_with_frequency['futex'], malicious_list_of_sysCall_with_frequency_1['futex'], malicious_list_of_sysCall_with_frequency_2['futex'], malicious_list_of_sysCall_with_frequency_3['futex'], malicious_list_of_sysCall_with_frequency_4['futex'], malicious_list_of_sysCall_with_frequency_5['futex'], malicious_list_of_sysCall_with_frequency_6['futex']]
# plt.plot(X, Y, label='futex')
Y = [benign_list_of_sysCall_with_frequency['sched_yield'], malicious_list_of_sysCall_with_frequency_1['sched_yield'], malicious_list_of_sysCall_with_frequency_2['sched_yield'], malicious_list_of_sysCall_with_frequency_3['sched_yield'], malicious_list_of_sysCall_with_frequency_4['sched_yield'], malicious_list_of_sysCall_with_frequency_5['sched_yield'], malicious_list_of_sysCall_with_frequency_6['sched_yield']]
plt.plot(X, Y, label='sched_yield')
Y = [benign_list_of_sysCall_with_frequency['getpid'], malicious_list_of_sysCall_with_frequency_1['getpid'], malicious_list_of_sysCall_with_frequency_2['getpid'], malicious_list_of_sysCall_with_frequency_3['getpid'], malicious_list_of_sysCall_with_frequency_4['getpid'], malicious_list_of_sysCall_with_frequency_5['getpid'], malicious_list_of_sysCall_with_frequency_6['getpid']]
plt.plot(X, Y, label='getpid')
Y = [benign_list_of_sysCall_with_frequency['poll'], malicious_list_of_sysCall_with_frequency_1['poll'], malicious_list_of_sysCall_with_frequency_2['poll'], malicious_list_of_sysCall_with_frequency_3['poll'], malicious_list_of_sysCall_with_frequency_4['poll'], malicious_list_of_sysCall_with_frequency_5['poll'], malicious_list_of_sysCall_with_frequency_6['poll']]
plt.plot(X, Y, label='poll')
Y = [benign_list_of_sysCall_with_frequency['shutdown'], malicious_list_of_sysCall_with_frequency_1['shutdown'], malicious_list_of_sysCall_with_frequency_2['shutdown'], malicious_list_of_sysCall_with_frequency_3['shutdown'], malicious_list_of_sysCall_with_frequency_4['shutdown'], malicious_list_of_sysCall_with_frequency_5['shutdown'], malicious_list_of_sysCall_with_frequency_6['shutdown']]
plt.plot(X, Y, label='shutdown')
Y = [benign_list_of_sysCall_with_frequency['ppoll'], malicious_list_of_sysCall_with_frequency_1['ppoll'], malicious_list_of_sysCall_with_frequency_2['ppoll'], malicious_list_of_sysCall_with_frequency_3['ppoll'], malicious_list_of_sysCall_with_frequency_4['ppoll'], malicious_list_of_sysCall_with_frequency_5['ppoll'], malicious_list_of_sysCall_with_frequency_6['ppoll']]
plt.plot(X, Y, label='ppoll')
Y = [benign_list_of_sysCall_with_frequency['accept'], malicious_list_of_sysCall_with_frequency_1['accept'], malicious_list_of_sysCall_with_frequency_2['accept'], malicious_list_of_sysCall_with_frequency_3['accept'], malicious_list_of_sysCall_with_frequency_4['accept'], malicious_list_of_sysCall_with_frequency_5['accept'], malicious_list_of_sysCall_with_frequency_6['accept']]
plt.plot(X, Y, label='accept')
Y = [benign_list_of_sysCall_with_frequency['gettid'], malicious_list_of_sysCall_with_frequency_1['gettid'], malicious_list_of_sysCall_with_frequency_2['gettid'], malicious_list_of_sysCall_with_frequency_3['gettid'], malicious_list_of_sysCall_with_frequency_4['gettid'], malicious_list_of_sysCall_with_frequency_5['gettid'], malicious_list_of_sysCall_with_frequency_6['gettid']]
plt.plot(X, Y, label='gettid')
Y = [benign_list_of_sysCall_with_frequency['getpeername'], malicious_list_of_sysCall_with_frequency_1['getpeername'], malicious_list_of_sysCall_with_frequency_2['getpeername'], malicious_list_of_sysCall_with_frequency_3['getpeername'], malicious_list_of_sysCall_with_frequency_4['getpeername'], malicious_list_of_sysCall_with_frequency_5['getpeername'], malicious_list_of_sysCall_with_frequency_6['getpeername']]
plt.plot(X, Y, label='getpeername')
Y = [benign_list_of_sysCall_with_frequency['close'], malicious_list_of_sysCall_with_frequency_1['close'], malicious_list_of_sysCall_with_frequency_2['close'], malicious_list_of_sysCall_with_frequency_3['close'], malicious_list_of_sysCall_with_frequency_4['close'], malicious_list_of_sysCall_with_frequency_5['close'], malicious_list_of_sysCall_with_frequency_6['close']]
plt.plot(X, Y, label='close')
Y = [benign_list_of_sysCall_with_frequency['io_getevents'], malicious_list_of_sysCall_with_frequency_1['io_getevents'], malicious_list_of_sysCall_with_frequency_2['io_getevents'], malicious_list_of_sysCall_with_frequency_3['io_getevents'], malicious_list_of_sysCall_with_frequency_4['io_getevents'], malicious_list_of_sysCall_with_frequency_5['io_getevents'], malicious_list_of_sysCall_with_frequency_6['io_getevents']]
plt.plot(X, Y, label='io_getevents')
Y = [benign_list_of_sysCall_with_frequency['nanosleep'], malicious_list_of_sysCall_with_frequency_1['nanosleep'], malicious_list_of_sysCall_with_frequency_2['nanosleep'], malicious_list_of_sysCall_with_frequency_3['nanosleep'], malicious_list_of_sysCall_with_frequency_4['nanosleep'], malicious_list_of_sysCall_with_frequency_5['nanosleep'], malicious_list_of_sysCall_with_frequency_6['nanosleep']]
plt.plot(X, Y, label='nanosleep')
plt.xlabel('Number of Manipulated fields')
plt.ylabel('Frequency of syscall')
plt.title('Frequency of System calls with number of manipulated fields')
plt.legend()
plt.show()
# Both = [value for value in benign_list_of_sysCall_with_frequency if value in malicious_list_of_sysCall_with_frequency]
# print(Both)

# count=0
# for i in range(0,len(Both)):
#     if (abs(benign_list_of_sysCall_with_frequency[Both[i]] - malicious_list_of_sysCall_with_frequency[Both[i]]) / benign_list_of_sysCall_with_frequency[Both[i]]) > 0.3 and malicious_list_of_sysCall_with_frequency[Both[i]] > 10:
#         count = count+1
#         SysCall_name.append(Both[i])
#         mal_SysCall_frequency.append(malicious_list_of_sysCall_with_frequency[Both[i]])
#         ben_SysCall_frequency.append(benign_list_of_sysCall_with_frequency[Both[i]])
# print(count)

