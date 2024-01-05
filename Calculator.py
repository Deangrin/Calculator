from Operators import OPERATORS
from CalculatorException import CalculatorException


def remove_minuses(num):
    """
    removes redundant minuses from given number - cleaning a number from minuses
    :param num: number to clean
    :return: number after cleaning
    """
    i = 0
    while i < len(num) and num[i] == '-':
        i += 1
    if i % 2 == 0:
        return num[i:]
    return "-" + num[i:]


def construct_number(exp, i):
    """
    constructs a number from a given index in an expression
    :param exp: string expression containing the number
    :param i: index of beginning of number in the expression
    :return: the constructed number and its length in the expression
    """
    num = exp[i]
    pos = i + 1
    if num == '-':
        while i < len(exp) and exp[pos] == '-':
            num += exp[pos]
            pos += 1
    while pos < len(exp) and (exp[pos].isdigit() or exp[pos] == '.'):
        num += exp[pos]
        pos += 1
    return num, pos - i


def previous_for_unary(term):
    """
    checks if received term placed before a minus indicates of unary minus
    :param term: term before minus
    :return: True if indicates unary minus, False if binary
    """
    return term == '(' or term in OPERATORS and OPERATORS[term].location != 2


def handle_term(exp, i):
    """
    handles a single term in a math expression
    :param exp: string math expression
    :param i: index of term to handle
    :return: the term and its length in the expression, or None for error
    """
    term = exp[i]
    if term not in OPERATORS and not term.isdigit() and term not in ('.', '(', ')'):
        print("invalid term:", term)
        raise CalculatorException
    elif term.isdigit() or term == '.' or term == '-' and (i == 0 or previous_for_unary(exp[i - 1])):
        term, length = construct_number(exp, i)
        try:
            term = float(remove_minuses(term))
        except ValueError:
            print(term, "not a number")
            raise CalculatorException
        return term, length
    else:
        return term, 1


def break_expression(exp):
    """
    breaks a math expression into individual terms
    :param exp: math expression to break
    :return: a list containing the terms of the given expression
    """
    terms = []
    i = 0
    exp = exp.replace(" ", "")
    while i < len(exp):
        term, length = handle_term(exp, i)
        terms.append(term)
        i += length
    return terms


def turn_postfix(infix):
    """
    turns an infix mathematical expression to its postfix representation
    :param infix: list of infix math expression
    :return: list of postfix math expression
    """
    stack = []  # doesn't work properly for unary expressions, makes them work when they shouldn't: !3, 3~ !!!!!!!!!!!!!!
    postfix = []
    for term in infix:
        if isinstance(term, float):
            postfix.append(term)
        elif term == '(':
            stack.append(term)
        elif term == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and OPERATORS[term].precedence <= OPERATORS[stack[-1]].precedence:
                postfix.append(stack.pop())
            stack.append(term)
    while stack:
        postfix.append(stack.pop())
    return postfix


def calculate_postfix(postfix):
    stack = []
    for term in postfix:
        if isinstance(term, float):
            stack.append(term)
        else:
            try:
                if OPERATORS[term].location == 1:
                    op2 = stack.pop()
                    op1 = stack.pop()
                    stack.append(OPERATORS[term].calc(op1, op2))
                else:
                    op = stack.pop()
                    stack.append(OPERATORS[term].calc(op))
            except (IndexError, TypeError):
                print("not enough operands for operator:", term)
                raise CalculatorException
    if len(stack) != 1:
        print("invalid expression - not enough operators for operands")
        raise CalculatorException
    return stack


def main():
    while True:
        try:
            exp = input("enter expression to calculate")
            infix = break_expression(exp)
            print(infix)
            postfix = turn_postfix(infix)
            print(postfix)
            result = calculate_postfix(postfix)
            print(result)
        except CalculatorException:
            pass


if __name__ == '__main__':
    main()
