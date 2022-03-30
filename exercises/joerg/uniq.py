def uniq(l):
    have = set()
    output = []
    for element in l:
        if element not in have:
            output.append(element)
            have.add(element)
    return output

input_list = [2, 3, 1, 10, 3, 3, 1, 10, 5, 2]
output_list = uniq(input_list)

for element in output_list:
    print(element)
