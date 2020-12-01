import csv
from os import listdir


CSV_files_list = [i for i in listdir(".") if i.endswith(".csv")]
try_number = len(CSV_files_list)
row_num = 1
row_ignore = [0]
dup_equal_more_than = 2
account_ignore = ["radiojavan", "taj_cover", "histofeed", "badall__",
                  "persingh.chale_lop.ana", "karafarin_m", "mobonews",
                  "gallery_gillda", "nails_ziba_33", "skincare_azimian",
                  "vancityreynolds", "astro.school", "matin_turism",
                  "shakella_beauty_sh.k", "realshadmehr", "farhadpaz",
                  "dr.shohre.geshnizjani", "opaz._.gallery", "billieeilish",
                  "oxkord", "iz.mohsen", "khandelaneh", "farzinemoon_s",
                  "sinavaliollah", "jashnvareh.tv", "nitrugen", "saburi_ali",
                  "shk__beauty", "homayounshajarian", "estekhdam_work_athome",
                  "jadijadinet", "coketell", "campazad", "atare.sadat.alavi",
                  "nik_yousefi", "chal_peirsing_khas", "physics_sadeghi",
                  "armanthefreak", "qomash_zarean", "arbeimohamd", "shahrekord.fun",
                  "danial_kheirikhah", "bahare_dehkordi", "grim.mohsen", "tarhemandegar20",
                  "rezam___mousavi", "fama_babai", "poshakavinaaa", "topaz._.gallery",
                  "amazing._.fact", "ina.saramy", "kzmi_nazanin", "mohammad.rabieifar"]

users = []
duplicates = []


for CSV in CSV_files_list:
    with open(CSV) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for index, row in enumerate(csv_reader):
            if index not in row_ignore:
                if row[row_num] not in users:
                    if row[row_num] not in account_ignore:
                        users.append(row[row_num])   # add unique users

                else:       # find duplicated users
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

def sorter(item):
    return item[1]

duplicates = [i for i in duplicates if i[1] >= dup_equal_more_than]

duplicates.sort(key=sorter, reverse=True)

print("Duplicated Usernames : {}".format(len(duplicates)))
print()

for i in duplicates:
    print(i)
input()
