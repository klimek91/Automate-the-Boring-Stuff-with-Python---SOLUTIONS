def collatz(number):
    if number % 2 == 0:
        print(int(number/2))
        collatz(number/2)
    elif number == 1:
        print('Collatz Compete')
    elif number % 2 != 0:
        print(int(3 * number +1))
        collatz(3 * number +1)

while True:
    try:
        collatz(int(input("Please enter integer greater than 1: ")))
        break
    except ValueError:
        print("Value error, You must enter integer")