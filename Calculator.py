OPERATORS = {'+': 1,
             '-': 1,
             '*': 2,
             '/': 2,
             '^': 3,
             '@': 5,
             '$': 5,
             '&': 5,
             '%': 4,
             '~': 6,
             '!': 6}


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
        return None
    elif term.isdigit() or term == '.' or (term == '-' and (i == 0 or exp[i - 1] in OPERATORS)):
        term, length = construct_number(exp, i)
        try:
            term = float(remove_minuses(term))
        except ValueError:
            print(term, "not a number")
            return None
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
        term = handle_term(exp, i)
        if term is None:
            return term
        terms.append(term[0])
        i += term[1]
    return terms


def turn_postfix(infix):
    stack = []
    postfix = []
    for term in infix:
        if isinstance(term, float):
            postfix.append(term)
        elif term == '(':
            stack.append(term)
        elif term == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
        else:
            while stack and stack[-1] != '(' and OPERATORS[term] <= OPERATORS[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(term)
    while stack:
        postfix.append(stack.pop())
    return postfix


def main():
    while True:
        exp = input("enter expression to calculate")
        infix = break_expression(exp)
        if infix is None:
            continue


if __name__ == '__main__':
    main()
