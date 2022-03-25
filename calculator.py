def calculate():
    operation = input('''
    Please type in the math operation you would like to complete ->
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')
    number_1 = int(input('Enter your first number ->'))
    number_2 = int(input('Enter your second number ->'))

    if operation == '+':
        print('{} + {} ='.format(number_1, number_2), number_1 + number_2)

    elif operation == '-':
        print('{} - {} ='.format(number_1, number_2), number_1 - number_2)

    elif operation == '*':
        print('{} * {} ='.format(number_1, number_2), number_1 * number_2)
    elif operation == '/':
        if number_2 == 0:
            print("You can not divide by zero")
        else:
            print('{} / {} ='.format(number_1, number_2), number_1 / number_2)
    else:
        print('You have not typed a valid operator, please rerun a program')

    def again():
        calc_again = input('''
        Do you want to calculate again?
        Please type Y for YES or N for NO.
        ''')

        if calc_again.upper() == 'Y':
            calculate()
        elif calc_again.upper() == 'N':
            print('See you later)')
        else:
            again()

    again()


calculate()
