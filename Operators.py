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
        if (-1 < op2 < 0 or 0 < op2 < 1) and op1 < 0:
            print("cannot take a root out of a negative number")
            raise CalculatorException
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
        if not op.is_integer() or op < 0:
            print("factorial operand can only be a positive integer")
            raise CalculatorException
        if op <= 1:
            return 1
        return op * Factorial.calc(op - 1)


class Hash(object):
    """
    hash operator class
    """
    precedence = 6
    location = 2

    @staticmethod
    def calc(op):
        res = 0
        if op < 0:
            print("hash operand must be positive")
            raise CalculatorException
        for digit in str(op):
            if digit != '.':
                try:
                    res += int(digit)
                except ValueError:
                    print("cannot perform hash on this number (may be inf or nan)")
                    raise CalculatorException
        return res


class Negative(object):
    """
    unary minus operator class. not for use
    """
    precedence = 2.5  # hope this is what you meant in the document and not 3.5 :|
    location = 0

    @staticmethod
    def calc(op):
        return -op


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
             '!': Factorial,
             '#': Hash,
             '_': Negative}
