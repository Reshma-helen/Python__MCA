'''import csv
with open ('dep.csv') as files:
    data=csv.reader(files)
    for r in data:
        print(','.join(r))'''

import csv
with open ('dep.csv',newline='')as csvfile:
    data=csv.reader(csvfile,delimiter=' ',quotechar='|')
    for row in data:
        print(','.join(row))
