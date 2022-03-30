import sys
import csv


f = open(sys.argv[1], encoding='cp1252')
rdr = csv.DictReader(f, delimiter=';', quotechar='"')
for userdict in rdr:
    uid = userdict['ID']
    firstname = userdict['First name']
    lastname = userdict['Last name']
    birth = userdict['Date of Birth']

    print(f'ID:{uid}, Firstname:{firstname}, Lastname:{lastname}, Date of birth: {birth}')
