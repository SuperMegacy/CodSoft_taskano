#!/usr/bin/env python3

from pgenerator import PasswordGenerator, PasswordLengthError
import os

def main():
    p_gen = PasswordGenerator()
    p_geerated = ""

    while True:
        print('\tWelcome to the Password Generator program\n')
        print('====Password Complexity Menu===')
        print('1. Easy Password')
        print('2. Medium Password')
        print('3. Hard Password')
        print('4. Exit')

        try:
            p_level = int(input('Enter the Password Complexity: '))

            if p_level not in [1, 2, 3, 4]:
                raise ValueError('Invalid option: {}, Choose between 1 to 3'.format(p_level))
            
            if p_level == 4:
                print('\n======Thank you for using The Password Generator Program========\n')
                break

            if p_level == 1:
                p_length = int(input('Enter Password length of at least 4 characters: '))
                p_generated = p_gen.easy(p_length)
                #print(p_generated)
            elif p_level == 2:
                p_length = int(input('Enter Password length of at least 8 characters: '))
                p_generated = p_gen.medium(p_length)
                #print(p_generated)
            elif p_level == 3:
                p_length = int(input('Enter Password length of at least 12 characters: '))
                p_generated = p_gen.hard(p_length)
                #print(p_generated)

            print('\nYour Generated Password is: {}.'.format(p_generated))
            input('Press Enter key to continue...')
            os.system('clear')

        except ValueError as vr:
            print(f'Error: {vr}.')
        except TypeError as tp:
            print(f'Error: {tp}.')
        except PasswordLengthError as pl:
            print(f'Error: {pl}')



if __name__ == "__main__":
    main()

