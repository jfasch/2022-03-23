import sys

translation_table = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

try:
    digit_str = sys.argv[1]
    digit = int(digit_str)
    print(translation_table[digit])
except ValueError:
    print(f'{digit_str} is not a number')
except KeyError:
    print(f'{digit} is not a digit')
