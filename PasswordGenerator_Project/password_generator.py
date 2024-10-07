#!/usr/bin/env python3

import string
from random import choice

class PasswordLengthError(Exception):
    pass

print('=================Welcome to the Password Generator=================\n\n')

generated_password = ""

print('===Password complexity===\n')
print('1. Easy Password')
print('2. Medium Hard Password')
print('3. Hard Password\n')

try:
    password_level = int(input('please Enter the Password Complexity: '))

    if password_level not in [1, 2, 3]:
        raise ValueError(f'Invalid option: {password_level}. Please choose the complexity level between 1 and 3.')

    if password_level == 1:
        print('==Easy Password==')
        try:
            password_length = int(input('Enter the password length(Easy Password Length must be greater or equal to 4): '))
            if password_length < 4:
                raise PasswordLengthError(f'Password Length must be greater or equal to 4')

            characters = string.digits + string.ascii_lowercase
            generated_password = ''.join(random.choice(characters) for char in range(password_length))
            print(generated_password)

        except (ValueError, PasswordLengthError) as password_error:
            print(password_error)
        
    elif password_level == 2:

        try:
            password_length = int(input('Enter the password length(Easy Password Length must be greater or equal to 8): '))
            if password_length < 8:
                raise PasswordLengthError(f'Password Length must be greater or equal to 8')

            characters = string.ascii_letters + string.digits
            generated_password = ''.join(random.choice(characters) for char in range(password_length))
            print(generated_password)

        except (ValueError, PasswordLengthError) as password_error:
            print(password_error)

    elif password_level == 3:

        try:
            password_length = int(input('Enter the password length(Easy Password Length must be greater or equal to 12): '))
            if password_length < 12:
                raise PasswordLengthError(f'Password Length must be greater or equal to 12')

            characters = string.ascii_letters + string.digits + string.punctuation
            generated_password = ''.join(random.choice(characters) for char in range(password_length))
            print(generated_password)

        except (ValueError, PasswordLengthError) as password_error:
            print(password_error)


except ValueError as my_error:
    print(my_error)
