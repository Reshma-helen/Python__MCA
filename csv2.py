import csv
with open('dep.csv')as files:
    data=csv.reader(files)
    for row in data:
        #print(row[0])
        #print(row[1])
        #print(row[2])
        print(row[0],row[1],row[2])
