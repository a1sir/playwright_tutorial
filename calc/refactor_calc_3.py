#!/usr/bin/env python3

class Calc:

    def __init__(self):
        self.a_var = None
        self.b_var = None
        self.operation = None

    # Перечень доступных функций - сложение, вычитание, умножение, деление (целочисленное), возведение в степень
    # Операция сложения
    def addition(self, a, b):
        result = a + b
        return result

    # Операция вычитания
    def subtract(self, a, b):
        result = a - b
        return result

    # Операция умножения
    def multiplication(self, a, b):
        result = a * b
        return result

    # Операция целочисленного деления
    def division(self, a, b):
        try:
            result = a // b
            return result
        except ZeroDivisionError:
            print("Ошибка: нельзя делить на ноль")


    # Операция возведения в степень
    def exponentiation(self, a, b):
        result = a ** b
        return result

    # Остаток от деления
    def remainder(self, a, b):
        try:
            result = a % b
            return result
        except ZeroDivisionError:
            print("Ошибка: нельзя делить на ноль")

    def ask_oper(self):
        message = '''
Укажите выбираемую операцию через символ (сложение (+), вычитание (-), деление (/), умножение (*), возведение в степень \
(** or ^), остаток от деления (%):
Ваша операция:
           '''
        # Запрос действия у пользователя
        oper = input(message)
        return oper

    # Исключение, если вводим строку вместо числа
    def input_var(self, message):
        # Ввод переменной
        data = None
        while data is None:
            try:
                data = int(input(message))
            except ValueError:
                print("Необходимо ввести число")
        return data


    # Условные операторы для функций
    def calculate(self, a_var, b_var, operation):
        result = None
        if operation == '+':
            result = self.addition(a_var, b_var)
        elif operation == '-':
            result = self.subtract(a_var, b_var)
        elif operation == '/':
            result = self.division(a_var, b_var)
        elif operation == '*':
            result = self.multiplication(a_var, b_var)
        elif operation == '^' or operation == '**':
            result = self.exponentiation(a_var, b_var)
        elif operation == '%':
            result = self.remainder(a_var, b_var)
        else:
            print('Неизвестная операция')
        return result


def main():
    calc = Calc()
    a_var = calc.input_var('Введите первое число: ')
    b_var = calc.input_var('Введите второе число: ')
    oper = calc.ask_oper()
    calc_rez = calc.calculate(a_var, b_var, oper)
    print(f'Результат вычислений: {calc_rez}')

if __name__ == '__main__':
    main()
