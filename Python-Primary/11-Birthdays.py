birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 23', 'Carol': 'Mar 4'}

while True:
    name = input('Enter a name: (blank to quit) ')
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday info for ' + name)
        bday = input('What is their birthday? ')
        birthdays[name] = bday
        print('Birthdays database updated.')

