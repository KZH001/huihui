import csv

# writer = csv.writer(open('csvfile.xls','wb'))
reader = csv.reader(open('csvfile.xls','rb'))

# writer.writerow(['a','b','c'])

for line in reader:
    print line
