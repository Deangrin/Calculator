from Operators import OPERATORS
from CalculatorException import CalculatorException


def count_minuses(exp, i):
    """
    counts the number of consecutive minuses at a given index in an expression
    :param exp: string expression containing minuses
    :param i: index in expression in which the minus count will begin
    :return: number of consecutive minuses beginning in index i
    """
    count = 0
    while i + count < len(exp) and exp[i + count] == '-':
        count += 1
    return count


def construct_number(exp, i):
    """
    constructs a number from a given index in an expression
    :param exp: string expression containing the number
    :param i: index of beginning of number in the expression
    :return: the constructed number and its original length in the expression
    """
    num = ""
    pos = i
    if exp[pos] == '-':
        minuses = count_minuses(exp, pos)
        pos += minuses
        if minuses % 2 == 1:
            num = "-"
    while pos < len(exp) and (exp[pos].isdigit() or exp[pos] == '.'):
        num += exp[pos]
        pos += 1
    return num, pos - i


def handle_term(exp, i):
    """
    handles a single term in a math expression
    :param exp: string math expression
    :param i: index of term to handle
    :return: the term and its length in the original expression
    """
    term = exp[i]
    if term == '_' or term not in OPERATORS and not term.isdigit() and term not in ('.', '(', ')'):
        print("invalid term:", term)
        raise CalculatorException
    elif term.isdigit() or term == '.' or term == '-' and (i != 0 and exp[i - 1] in OPERATORS
                                                           and OPERATORS[exp[i - 1]].location != 2):
        term, length = construct_number(exp, i)
        try:
            term = float(term)
        except ValueError:
            print(term, "not a number")
            raise CalculatorException
        return term, length
    elif term == '-' and (i == 0 or exp[i - 1] == '('):
        minuses = count_minuses(exp, i)
        if minuses % 2 == 1:
            return '_', minuses
        return None, minuses
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
    exp = exp.replace(" ", "").replace("\t", "")
    while i < len(exp):
        term, length = handle_term(exp, i)
        if term is not None:
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
    """
    calculates a mathematical expression in postfix representation
    :param postfix: list of postfix math expression
    :return: calculation result of math expression
    """
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
        print("invalid expression")
        raise CalculatorException
    return stack.pop()


def main():
    while True:
        try:
            exp = input("enter expression to calculate ")
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
