def collatz(number):
    if number % 2 == 0:
        return number // 2
    return number * 3 + 1

print('Enter a number: ', end='')

try:
    num = int(input())
    print('Collatz sequence: ', end='')
    while num != 1:
        print(str(collatz(num)), end=' ')
        num = collatz(num)
    print()

# If user gives an input without an integer
except ValueError:
    print('Please enter an integer number.')
