import sys
import csv


f = open(sys.argv[1], encoding='cp1252')
rdr = csv.reader(f, delimiter=';', quotechar='"')
for id, firstname, lastname, birth in rdr:
    print(f'ID:{id}, Firstname:{firstname}, Lastname:{lastname}, Date of birth: {birth}')
