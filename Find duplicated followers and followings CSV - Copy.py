import csv
from os import listdir


CSV_files_list = [i for i in listdir(".") if i.endswith(".csv")]
try_number = len(CSV_files_list)
row_num = 1
row_ignore = [0]

users = []
duplicates = []


for CSV in CSV_files_list:
    with open(CSV) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for index, row in enumerate(csv_reader):
            if index not in row_ignore:
                if row[row_num] not in users:
                    users.append(row[row_num])

                else:
                    x = 1
                    dont_have = False
                    
                    while x <= try_number:
                        if not dont_have:
                            if (row[row_num], x) in duplicates:
                                dont_have = True
                                duplicates.remove((row[row_num], x))
                                duplicates.append((row[row_num], x+1))
                        x += 1

                    if not dont_have:
                       duplicates.append((row[row_num], 2))

duplicates = list(set(duplicates))

print("Duplicated Usernames : {}".format(len(duplicates)))
print()

for i in duplicates:
    print(i)
input()