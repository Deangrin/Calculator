from CalculatorException import CalculatorException


class Plus(object):
    """
    plus operator class
    """
    precedence = 1
    location = 1

    @staticmethod
    def calc(op1, op2):
        return op1 + op2


class Minus(object):
    """
    minus operator class
    """
    precedence = 1
    location = 1

    @staticmethod
    def calc(op1, op2):
        return op1 - op2


class Mult(object):
    """
    multiplication operator class
    """
    precedence = 2
    location = 1

    @staticmethod
    def calc(op1, op2):
        return op1 * op2


class Div(object):
    """
    division operator class
    """
    precedence = 2
    location = 1

    @staticmethod
    def calc(op1, op2):
        try:
            return op1 / op2
        except ZeroDivisionError:
            print("cannot divide by zero")
            raise CalculatorException


class Power(object):
    """
    power operator class
    """
    precedence = 3
    location = 1

    @staticmethod
    def calc(op1, op2):
        return op1 ** op2


class Avg(object):
    """
    average operator class
    """
    precedence = 5
    location = 1

    @staticmethod
    def calc(op1, op2):
        return (op1 + op2) / 2


class Max(object):
    """
    maximum operator class
    """
    precedence = 5
    location = 1

    @staticmethod
    def calc(op1, op2):
        return max(op1, op2)


class Min(object):
    """
    minimum operator class
    """
    precedence = 5
    location = 1

    @staticmethod
    def calc(op1, op2):
        return min(op1, op2)


class Modulo(object):
    """
    modulo operator class
    """
    precedence = 4
    location = 1

    @staticmethod
    def calc(op1, op2):
        return op1 % op2


class Tilde(object):
    """
    tilde operator class
    """
    precedence = 6
    location = 0

    @staticmethod
    def calc(op):
        return -op


class Factorial(object):
    """
    factorial operator class
    """
    precedence = 6
    location = 2

    @staticmethod
    def calc(op):
        if not isinstance(op, int) or op < 0:
            print("factorial operator can only be a positive integer")
            raise CalculatorException
        if op <= 1:
            return 1
        return op * Factorial.calc(op - 1)


OPERATORS = {'+': Plus,
             '-': Minus,
             '*': Mult,
             '/': Div,
             '^': Power,
             '@': Avg,
             '$': Max,
             '&': Min,
             '%': Modulo,
             '~': Tilde,
             '!': Factorial}
