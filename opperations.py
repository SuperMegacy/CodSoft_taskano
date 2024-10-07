import os

class Calculator:
    def __init__(self) -> None:
        self.__results = 0
        self.__history = []

    def add(self, a: float, b: float) -> float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError('Both Number 1 and Number 2 must be digits')

        self.__results = a + b
        self.__history.append('{} + {} = {}'.format(a, b, self.__results))
        return self.__results
    
    def sub(self, a: float, b: float) -> float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError('Both Number 1 and Number 2 must be digits')

        self.__results = a - b
        self.__history.append('{} - {} = {}'.format(a, b, self.__results))
        return self.__results

    def mult(self, a: float, b: float) -> float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError('Both Number 1 and Number 2 must be digits')

        self.__results = a * b
        self.__history.append('{} * {} = {}'.format(a, b, self.__results))
        return self.__results

    def div(self, a: float, b: float) -> float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError('Both Number 1 and Number 2 must be digits')

        try:
            self.__results = a / b
            self.__history.append('{} / {} = {}'.format(a, b, self.__results))
            return self.__results
        except ZeroDivisionError:
            return 'Cannot Devide by Zero'

    def gethistory(self) -> None:
        if not self.__history:
            print("No History yet")

        else:
            print('Calculator History: ')
            for my_history in self.__history:
                print(my_history)

    def clearhistory(self) -> list:
        if not self.__history:
            print('No History')
        else:
            self.__history = []
            print('History cleared')
            return self.__history

    def clear_screen(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')