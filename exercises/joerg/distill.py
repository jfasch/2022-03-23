import sys

filename = sys.argv[1]
f = open(filename)

for line in f:
    line = line.rstrip('\n')
    orig_line = line

    comment_pos = line.find('#')
    if comment_pos != -1:
        line = line[:comment_pos]
    if len(line.strip()) == 0:
        continue

    print(orig_line)
