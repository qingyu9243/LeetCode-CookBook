import os

#print("a")

file_dir = "lab_data.csv"

sum_of_labs = 0
mean_of_labs = 0
medium_of_labs = 0
data = []
data_lab_nums = []

with open(file_dir,'r') as reader:
    for line in reader.readlines():
        s = line.split(',')
        data.append(s)
        if s[0].isdigit():
            index, patient_name, number_labs = s[0], s[1], s[2]
            sum_of_labs += int(number_labs)
            data_lab_nums.append(int(number_labs))

data_length = len(data)-1
mean_of_labs = sum_of_labs/data_length

data_lab_nums.sort()
print(data_lab_nums)
if data_length % 2 != 0:
    medium_of_labs = data_lab_nums[data_length//2]
else:
    medium_of_labs = (int(data_lab_nums[data_length//2]) + int(data_lab_nums[data_length//2-1]))/2

print("sum num of labs", sum_of_labs)
print("mean num of labs", mean_of_labs)
print("medium num of labs", medium_of_labs)