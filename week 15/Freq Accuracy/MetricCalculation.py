import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Set the font size for various elements
mpl.rcParams['axes.labelsize'] = 16
mpl.rcParams['axes.titlesize'] = 16
mpl.rcParams['xtick.labelsize'] = 12
mpl.rcParams['ytick.labelsize'] = 14
mpl.rcParams['legend.fontsize'] = 16

def caluclateMetrics(tp, tn, fp, fn):
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    return accuracy, precision, recall, f1_score

ImpactField = []
ImpactField.append(caluclateMetrics(80,97,4,20))
ImpactField.append(caluclateMetrics(84,97,4,17))
ImpactField.append(caluclateMetrics(94,97,4,7))
ImpactField.append(caluclateMetrics(97,97,4,4))
ImpactField.append(caluclateMetrics(97,97,4,4))
ImpactField.append(caluclateMetrics(100,97,4,0))
print(ImpactField)

#plot accuracy vs impact field
x = [1,2,3,4,5,6]
Accuracy = []
Precision = []
Recall = []
F1_Score = []
for i in range(len(ImpactField)):
    Accuracy.append(ImpactField[i][0])
    Precision.append(ImpactField[i][1])
    Recall.append(ImpactField[i][2])
    F1_Score.append(ImpactField[i][3])
plt.plot(x, Accuracy, label = "Accuracy", linestyle='-.')
plt.plot(x, Precision, label = "Precision", linestyle='--')
plt.plot(x, Recall, label = "Recall", linestyle=':')
plt.plot(x, F1_Score, label = "F1 Score",linestyle='-')
plt.xlabel('Number of Impacted Field', fontsize=16)
plt.ylabel('Metrics Values', fontsize=16)
plt.title('Metrics vs Impact Field using Frequency')
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()

