import sys

max = int(sys.argv[1])


num = 0
while num < max:
    if num % 2 == 0:
        print(num)
    num += 1
