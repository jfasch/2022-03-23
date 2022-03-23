import sys


sextable = {
    'm': 'Mr.',
    'f': 'Mrs.',
    'd': 'Prs.',
}

name = input('Name: ')

sex = input(f'Sex ({",".join(sextable.keys())}): ')
if sex not in sextable:
    print('Wrong sex')
    sys.exit(1)

hour_of_day = input('Hour of day (0-23): ')
hour_of_day = int(hour_of_day)
if hour_of_day not in range(0, 24):
    print('Wrong hour of day')
    sys.exit(1)

greeting = ''

if 0 <= hour_of_day <= 9:
    greeting += 'Good morning, '
elif 10 <= hour_of_day <= 17:
    greeting += 'Good day, '
else:
    greeting += 'Good evening, '

greeting += sextable[sex]
greeting += name

print(greeting)
