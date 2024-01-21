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
    while pos < len(exp) and (exp[pos].isdigit() or exp[pos] == '.'):
        num += exp[pos]
        pos += 1
    try:
        return float(num), pos - i
    except ValueError:
        raise CalculatorException(num + " not a number")


def handle_term(exp, i):
    """
    handles a single term in a math expression
    :param exp: string math expression
    :param i: index of term to handle
    :return: the term and its length in the original expression
    """
    term = exp[i]
    if term not in OPERATORS and not term.isdigit() and term not in ('.', '(', ')'):
        raise CalculatorException("invalid term: " + term)
    elif term.isdigit() or term == '.':
        return construct_number(exp, i)
    elif term == '-' and (i == 0 or exp[i-1] == '(' or exp[i-1] in OPERATORS and OPERATORS[exp[i-1]].location != 2):
        minuses = count_minuses(exp, i)
        valid_placement('- ', exp, i + minuses)
        if i == 0 or exp[i - 1] == '(':
            return ('- ', minuses) if minuses % 2 == 1 else (None, minuses)
        return ('-  ', minuses) if minuses % 2 == 1 else (None, minuses)
    else:
        return term, 1


def valid_placement(term, exp, i):
    """
    checks if given term and its following term (exp[i]) can be placed together
    :param term: current term
    :param exp: string math expression
    :param i: index of following term in expression
    :raise: CalculatorException if terms cannot be placed together, otherwise doesn't
    """
    if term in OPERATORS and OPERATORS[term].location == 0:
        if i >= len(exp) or exp[i] not in ('(', '.', '-') and not exp[i].isdigit():
            raise CalculatorException(term + " must be followed by a number, a minus or parentheses")
    elif ((term in OPERATORS and OPERATORS[term].location == 2 or term == ')' or isinstance(term, float))
          and i < len(exp)):
        if exp[i].isdigit() or exp[i] in ('(', '.') or exp[i] in OPERATORS and OPERATORS[exp[i]].location == 0:
            raise CalculatorException(str(term) + " cannot be followed by a number or parentheses")


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
            valid_placement(term, exp, i + length)
            terms.append(term)
        i += length
    return terms


def turn_postfix(infix):
    """
    turns an infix mathematical expression to its postfix representation
    :param infix: list of infix math expression
    :return: list of postfix math expression
    """
    stack = []
    postfix = []
    for term in infix:
        if isinstance(term, float):
            postfix.append(term)
        elif term == '(':
            stack.append(term)
        elif term == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            if not stack:  # can change for try, whatever is preferred...
                raise CalculatorException("unmatched closing parenthesis")
            stack.pop()
        else:
            while stack and stack[-1] != '(' and OPERATORS[term].precedence <= OPERATORS[stack[-1]].precedence:
                postfix.append(stack.pop())
            stack.append(term)
    while stack:
        if stack[-1] == '(':
            raise CalculatorException("unmatched opening parenthesis")
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
                    result = OPERATORS[term].calc(op1, op2)
                else:
                    op = stack.pop()
                    result = OPERATORS[term].calc(op)
                if result == float('inf'):
                    raise OverflowError
                if result == float('nan'):
                    raise CalculatorException("undefined result")
            except (IndexError, TypeError):
                raise CalculatorException("not enough operands for operator " + term)
            except (OverflowError, RecursionError):
                raise CalculatorException("result is too large")
            stack.append(round(float(result), 10))
    if len(stack) != 1:
        raise CalculatorException("invalid expression")
    return stack.pop()


def calculator(exp):
    """
    calculates mathematical expressions
    :param exp: string math expression
    :return: calculation result of expression
    :raise: CalculatorException with informative message for incorrect expressions
    """
    infix = break_expression(exp)
    postfix = turn_postfix(infix)
    result = calculate_postfix(postfix)
    return result


def main():
    """
    runs the calculator - receives mathematical expressions and prints their calculation results
    """
    while True:
        try:
            exp = input("enter expression to calculate ")
            result = calculator(exp)
            print(result)
        except CalculatorException as e:
            print(e)
        except (EOFError, KeyboardInterrupt):
            print("\nexiting the calculator...")
            break


if __name__ == '__main__':
    main()
