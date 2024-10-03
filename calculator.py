from opperations import Calculator

def main():

    calculator_obj = Calculator()
    print('Welcome to Simple Calculator')
    while True:
        input('Press Enter to continue...')
        calculator_obj.clear_screen()

        print('''\nSimple Calculator\n
        1. Addition
        2. Subtraction
        3. Multiplation
        4. Division
        6. History
        7. Clear History
        8. Exit\n''')

        try:
            usr_choice = int(input('Enter your choice: '))
   
            if usr_choice == 6:
                calculator_obj.gethistory()
                continue

            if usr_choice == 7:
                calculator_obj.clearhistory()
                continue

            if usr_choice == 8:
                calculator_obj.clear_screen()
                print('\n\tThank you for using Simple Calculator\n')
                break
            try:
                num1 = float(input('Enter number1: '))
                num2 = float(input('Enter number2: '))

                if usr_choice == 1:
                    print('\n======Addition=====')
                    results = calculator_obj.add(num1, num2)
                    print(f'{num1} + {num2} = {int(results)}')
                elif usr_choice == 2:
                    print('\n======Subtraction======')
                    results = calculator_obj.sub(num1, num2)
                    print(f'{num1} - {num2} = {results}')
                elif usr_choice == 3:
                    print('\n======Multiplicating=====')
                    results = calculator_obj.mult(num1, num2)
                    print(f"{num1} * {num2} = {results}")
                elif usr_choice == 4:
                    print("\n======Division=======")
                    results = calculator_obj.div(num1, num2)
                    if results is not None:
                        print(f'{num1} / {num2} = {results}')
                else:
                    print('Ivalide Option!')
                    continue
            except ValueError:
                print('Enter only floats or ints')
                continue
        except ValueError:
            print('Enter only Numbers')
            continue

if __name__ == '__main__':
    main()