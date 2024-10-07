#!/usr/bin/env python3

import string
import random

print('=================Welcome to the Password Generator=================\n\n')

generated_password = ""

print('===Password complexity===\n')
print('1. Easy Password')
print('2. Medium Hard Password')
print('3. Hard Password\n')

try:
    password_length = int(input('Enter the Password Length: '))
    try:
        password_level = int(input('Enter the Password Complexity: '))
        
        if password_level not in [1, 2, 3]:
            raise ValueError(f'Invalid option: {password_level}. Please choose the complexity level between 1 and 3.')

        if password_level == 1:
            characters = string.digits + string.ascii_lowercase
            generated_password = ''.join(random.choice(characters) for char in range(password_length))
            print(generated_password)
        
        elif password_level == 2:
            characters = string.ascii_letters + string.digits
            generated_password = ''.join(random.choice(characters) for char in range(password_length))
            print(generated_password)

        elif password_level == 3:
            characters = string.ascii_letters + string.digits + string.punctuation
            generated_password = ''.join(random.choice(characters) for char in range(password_length))
            print(generated_password)

    except ValueError as my_error:
        print(my_error)
       

except ValueError:
    print('the length should only be a Number!')

