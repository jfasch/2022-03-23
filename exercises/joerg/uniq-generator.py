def uniq(l):
    have = set()
    for element in l:
        if element not in have:
            yield element
            have.add(element)

def squares(l):
    for element in l:
        yield element**2

input_list = [2, 3, 1, 10, 3, 3, 1, 10, 5, 2]
output = squares(uniq(input_list))

for element in output:
    print(element)
