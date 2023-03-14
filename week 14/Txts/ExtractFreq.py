import numpy as np
import matplotlib.pyplot as plt
malicious_list_of_sysCall_with_frequency = {}
benign_list_of_sysCall_with_frequency = {}

SysCall_name = []
mal_SysCall_frequency = []
ben_SysCall_frequency = []

for j in range(1, 6):
    data = []
    with open('benign '+str(j)+'.txt', 'r') as f:
        for row in f.read().strip().split("\n")[3:]:
            data.append(row.split(" "))
    # print(data)
    for i in range(len(data)):
        if data[i][3] in benign_list_of_sysCall_with_frequency:
            benign_list_of_sysCall_with_frequency[data[i][3]] += float(data[i][0])
        else:
            benign_list_of_sysCall_with_frequency[data[i][3]] = float(data[i][0])
for i in range(len(data)):
    benign_list_of_sysCall_with_frequency[data[i][3]] = benign_list_of_sysCall_with_frequency[data[i][3]]/5

for j in range(1, 6):
    data = []
    with open('mal6_'+str(j)+'.txt', 'r', encoding="ascii", errors="surrogateescape") as f:
        for row in f.read().strip().split("\n")[3:]:
            data.append(row.split(" "))
    print(data)
    for i in range(len(data)):
        if data[i][3] in malicious_list_of_sysCall_with_frequency:
            malicious_list_of_sysCall_with_frequency[data[i][3]] += float(data[i][0])
        else:
            malicious_list_of_sysCall_with_frequency[data[i][3]] = float(data[i][0])
for i in range(len(data)):
    malicious_list_of_sysCall_with_frequency[data[i][3]] = malicious_list_of_sysCall_with_frequency[data[i][3]]/5


Both = [value for value in benign_list_of_sysCall_with_frequency if value in malicious_list_of_sysCall_with_frequency]
print(Both)

count=0
for i in range(0,len(Both)):
    if (abs(benign_list_of_sysCall_with_frequency[Both[i]] - malicious_list_of_sysCall_with_frequency[Both[i]]) / benign_list_of_sysCall_with_frequency[Both[i]]) > 0.3 and malicious_list_of_sysCall_with_frequency[Both[i]] > 10:
        count = count+1
        SysCall_name.append(Both[i])
        mal_SysCall_frequency.append(malicious_list_of_sysCall_with_frequency[Both[i]])
        ben_SysCall_frequency.append(benign_list_of_sysCall_with_frequency[Both[i]])
print(count)

X = np.arange(len(SysCall_name))
plt.bar(X - 0.2, ben_SysCall_frequency, color = 'b', width = 0.4)
plt.bar(X + 0.2, mal_SysCall_frequency, color = 'orange', width = 0.4)
plt.xticks(X, SysCall_name)
plt.xlabel("SysCall Name")
plt.ylabel("Frequency")
plt.title("For Number of manupulated field = 6")
plt.show()
# plt.savefig('Frequency(#Fields=2).png')