class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def calculation(first_operand, second_operand, operator):
        if operator == '*':
            result = first_operand * second_operand
        elif operator == '+':
            result = first_operand + second_operand
        elif operator == '-':
            result = first_operand - second_operand
        elif operator == '/':
            if second_operand == 0:
                raise ArithmeticError("Деление на ноль")
            result = first_operand / second_operand
        else:
            raise ValueError("Неверный оператор: " + operator)
        return result

    @staticmethod
    def square_root_extraction(number):
        if number == 0.0:
            raise ArithmeticError("Извлечение корня из нуля")
        elif number < 0.0:
            raise ArithmeticError("Извлечение корня из отрицательного числа")
        else:
            square_root = number / 2.0
            t = square_root
            while t - square_root != 0.0:
                t = square_root
                square_root = (square_root + number / square_root) / 2.0
            return square_root

    @staticmethod
    def calculate_discount(purchase_amount, discount_percentage):
        if purchase_amount < 0 or discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Неверное значение")

        discount_amount = purchase_amount * (discount_percentage / 100)
        discounted_price = purchase_amount - discount_amount
        return discounted_price
