import sys
import csv


userdatabase = {}

filename = sys.argv[1]
usernames = sys.argv[2:]

f = open(filename, encoding='ascii')
rdr = csv.reader(f, delimiter=':')

for user, passwd, uid, gid, description, home, shell in rdr:
    userdatabase[user] = {
        'user': user,
        'uid': uid,
        'gid': gid,
        'description': description,
        'home': home,
        'shell': shell,
    }


for user in usernames:
    metadata = userdatabase[user]

    print(f'''User: {metadata['user']}
  UID: {metadata['uid']}
  GID: {metadata['gid']}
  Home: {metadata['home']}
  Shell: {metadata['shell']}''')
    
