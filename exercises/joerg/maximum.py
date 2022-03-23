import sys

try:
    l = int(sys.argv[1])
    r = int(sys.argv[2])
except ValueError:
    print('nix integer')
    sys.exit(1)

if l < r:
    print(r)
else:
    print(l)
