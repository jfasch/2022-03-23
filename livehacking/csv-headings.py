import csv

f = open('escaped.csv')
rdr = csv.DictReader(f, delimiter=',', quotechar='"')
for metadata in rdr:
    num = metadata['ID']
    firstname = metadata['Firstname']
    lastname = metadata['Lastname']

    print(f'ID: {num} --- First name: {firstname} - Last name: {lastname}')
