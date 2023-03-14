import os
dir_name = "E:\study materials\Everything of 4-1\Thesis\week 15\Freq Accuracy"
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".txt"):
        os.remove(os.path.join(dir_name, item))