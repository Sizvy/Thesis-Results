import numpy as np
StandardAnomalousSyscalls = []
SystemcallTobeAnalyzed = []

with open("anomalousSyscalls.out", "r") as f:
    for line in f:
        flag = 0
        for i in range(0, len(StandardAnomalousSyscalls)):
            if line.startswith("---"):
                line = line.split(" ")[1] + '('
            if(StandardAnomalousSyscalls[i] == line.split("(")[0]):
                flag = 1
                break;
        if flag == 0:
            StandardAnomalousSyscalls.append(line.split("(")[0])

print(StandardAnomalousSyscalls)

with open("fileTobeAnalysed.out", "r") as f:
    for line in f:
        flag = 0
        for i in range(0, len(SystemcallTobeAnalyzed)):
            if(SystemcallTobeAnalyzed[i] == line.split("(")[0]):
                flag = 1
                break;
        if flag == 0:
            SystemcallTobeAnalyzed.append(line.split("(")[0])

print(SystemcallTobeAnalyzed)

count = 0
for i in range(0, len(SystemcallTobeAnalyzed)):
    for j in range(0, len(StandardAnomalousSyscalls)):
        if StandardAnomalousSyscalls[j] == SystemcallTobeAnalyzed[i]:
            count = count+1
            print(SystemcallTobeAnalyzed[i])

print(count*100/len(SystemcallTobeAnalyzed), "%")