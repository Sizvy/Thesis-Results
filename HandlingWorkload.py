import numpy as np
import os
from datetime import datetime

def parse_datetime_with_high_precision(input_str):
    time_parts = input_str.split(':')
    hour = int(time_parts[0])
    minute = int(time_parts[1])

    # Split the seconds part into seconds and microseconds
    seconds_with_micros = time_parts[2].split('.')
    second = int(seconds_with_micros[0])

    # Ensure we have exactly 6 digits for microseconds
    microsecond_str = seconds_with_micros[1][:6].ljust(6, '0')
    microsecond = int(microsecond_str)
    return datetime(1, 1, 1, hour, minute, second, microsecond)



# read line by line from a txt file
def read_file(file_name):
    with open(file_name, 'r') as f:
        data = f.readlines()
    return data



# Preprocess the data from a txt file 
def preprocess_data(data):
    j = 0
    New_data = []
    for i in range(len(data)):
        if i % 2 == 0:
            continue
        # Tokenize each line by space
        data[i] = data[i].split()
        # Insert every first element as long int and second element as timestamp in a list
        a = parse_datetime_with_high_precision(data[i][1])
        New_data.append([int(data[i][0]), a])
        # print(data[i])
    return New_data



# Categorize the file as benign or malicious
def categorize_file(data):
    # check the serial difference and time difference between two consecutive serial number
    for i in range(len(data)-1):
        serial_difference =  data[i+1][0] - data[i][0]
        time_difference = data[i+1][1] - data[i][1]
        # if(serial_difference > 40000):
        #     print(data[i][0], data[i][1], data[i+1][0], data[i+1][1])
        #     print(serial_difference, time_difference.seconds)
        if serial_difference > 40000:
            if time_difference.seconds <= 0:
                if(time_difference.microseconds < 999999):
                    print('Malicious')
                    return
            

# Iterate all files from a directory
sourceFolder = r'E:\study materials\\Everything of 4-1\\All works about thesis\\UnknownWeek 1\\io_submit\\'
for file_name in os.listdir(sourceFolder):
    print(file_name)
    sourceFile = sourceFolder + file_name
    data = read_file(sourceFile)
    # print(len(data))
    data = preprocess_data(data)
    # print(len(data))
    categorize_file(data)


