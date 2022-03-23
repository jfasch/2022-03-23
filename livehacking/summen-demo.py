import sys

if len(sys.argv) != 3:
    print('nix drei args')
    sys.exit(1)

argument1 = sys.argv[1]
argument2 = sys.argv[2]

summe = int(argument1) + int(argument2)

print(summe)
