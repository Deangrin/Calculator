from CalculatorException import CalculatorException


class Add(object):
    """
    plus operator class
    """
    precedence = 1
    location = 1

    @staticmethod
    def calc(op1, op2):
        return op1 + op2


class Sub(object):
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
            raise CalculatorException("cannot divide by zero")


class Power(object):
    """
    power operator class
    """
    precedence = 3
    location = 1

    @staticmethod
    def calc(op1, op2):
        if (-1 < op2 < 0 or 0 < op2 < 1) and op1 < 0:
            raise CalculatorException("cannot take a root out of a negative number")
        try:
            return op1 ** op2
        except ZeroDivisionError:
            raise CalculatorException("zero cannot be raised by a negative power")


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
        try:
            return op1 % op2
        except ZeroDivisionError:
            raise CalculatorException("cannot take modulo by zero")


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
            raise CalculatorException("factorial operand can only be a positive integer")
        if op <= 1:
            return 1.0
        return op * Factorial.calc(op - 1)


class Hash(object):
    """
    hash operator class
    """
    precedence = 6
    location = 2

    @staticmethod
    def calc(op):
        res = 0.0
        if op < 0:
            raise CalculatorException("hash operand must be positive")
        for digit in str(op):
            if digit != '.':
                res += int(digit)
        return res


class Minus(object):
    """
    unary minus operator class
    """
    precedence = 2.5  # hope this is what you meant in the document and not 3.5 :|
    location = 0

    @staticmethod
    def calc(op):
        return -op


class Negative(object):
    """
    negative sign operator class
    """
    precedence = 100
    location = 0

    @staticmethod
    def calc(op):
        return -op


# available operators
OPERATORS = {'+': Add,
             '-': Sub,
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
             '- ': Minus,
             '-  ': Negative}
