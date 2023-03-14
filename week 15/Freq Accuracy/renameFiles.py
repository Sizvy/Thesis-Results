import os

folder = 'E:\study materials\Everything of 4-1\Thesis\week 15\Freq Accuracy\Benign Text Versions(Testing Data)\\'
# destinationFolder = 'E:\study materials\Everything of 4-1\Thesis\week 15\Freq Accuracy\Malicious1 Text Versions\\'
count = 1
# count increase by 1 in each iteration
# iterate all files from a directory
for file_name in os.listdir(folder):
    # Construct old file name
    source = folder + file_name

    # Adding the count to the new file name and extension
    destination = folder + "Benign_" + str(count) + ".txt"

    # Renaming the file
    os.rename(source, destination)
    count += 1
print('All Files Renamed')