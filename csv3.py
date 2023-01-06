'''import csv
csv_columns = ['id','Column1', 'Column2', 'Column3', 'Column4', 'Column5']
dict_data = {'id':['1', '2', '3'],
    'Column1':[33, 25, 56],
    'Column2':[35, 30, 30],
    'Column3':[21, 40, 55],
    'Column4':[71, 25, 55],
    'Column5':[10, 10, 40], }
csv_file = "temp.csv"
try:
   with open(csv_file, 'w') as csvfile:
       writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
       writer.writeheader()
       for data in dict_data:
           writer.writerow(dict_data)
except IOError:
   print("I/O error")
data = csv.DictReader(open(csv_file))
print("CSV file as a dictionary:\n")
for row in data:
   print(row)'''

import csv
with open('new1.csv','w') as outf:
    fields = ['Name', 'Department', 'Birthday Month']
    content = csv.DictWriter(outf, fieldnames=fields)
    content.writeheader()
    content.writerow({'Name': 'John', 'Department': 'Accounts', 'Birthday Month': 'November'})
    content.writerow({'Name': 'Amy', 'Department': 'IT', 'Birthday Month': 'March'})

with open('new1.csv','r') as f:
    data=csv.reader(f)
    for r in data:
        print(','.join(r))
