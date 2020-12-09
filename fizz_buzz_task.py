print('Please, enter three numbers!')
fizz = int(input('Enter first number: '))
buzz = int(input('Enter second number: '))
count = int(input('Enter first number: '))

for num in range(1, count + 1):
    if num % fizz == 0 and num % buzz == 0:
        print('FB')
    elif num % fiz == 0:
        print('F')
    elif num % buzz == 0:
        print('B')
    else:
        print(num)
