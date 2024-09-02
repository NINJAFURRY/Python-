import sys
def collatz(number):
    if number % 2 == 0:
        num = number // 2
    elif number % 2 == 1:
        num = 3 * number + 1
    print(num)
    return num

try:
    print("Enter your number := ", end='')
    result = collatz((int(input())))
    while result != 1:
        result = collatz(result)
        if result == 1:
            print('You have got your 1 at the last')
    
except ValueError:
    print('You entered an string instead of intiger')
    sys.exit()
    



