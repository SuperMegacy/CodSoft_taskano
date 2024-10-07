import random
import string

class PasswordLengthError(Exception):
    pass


class PasswordGenerator(PasswordLengthError):
    def __init__(self):
        self.__generated_password = ""


    def __checkpaswordlength(self, password_length: int, min_length: int) -> None:
        """check the password length and type"""
        if not isinstance(password_length, int):
            raise TypeError(f'Password length must be a Number, got {type(password_length).__name__}.')

        if password_length < min_length:
            raise PasswordLengthError(f'Password length must be at least {min_length} characters.')


    def easy(self, password_length: int) -> str:
        #check if password length is >= 4
        #if less raise PasswordLengthError
        self.__checkpaswordlength(password_length, 4)

        characters = string.digits + string.ascii_lowercase
        self.__generated_password = ''.join(random.choice(characters) for chr in range(password_length))
        return self.__generated_password

    def medium(self, password_length: int) -> str:
        #want to check if password length is >= 8
        #if less raise PasswordLengthError
        self.__checkpaswordlength(password_length, 8)

        characters = string.digits + string.ascii_letters
        self.__generated_password = ''.join(random.choice(characters) for chr in range(password_length))
        return self.__generated_password

    def hard(self, password_length: int) -> str:
        #want to check if password length is >= 4
        #if less raise PasswordLengthError
        self.__checkpaswordlength(password_length, 4)

        characters = string.digits + string.ascii_letters + string.punctuation
        self.__generated_password = ''.join(random.choice(characters) for chr in range(password_length))
        return self.__generated_password

