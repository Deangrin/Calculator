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
    ch = exp[i]
    pos = i + 1
    if ch == '-':
        while i < len(exp) and exp[pos] == '-':
            ch += exp[pos]
            pos += 1
    while pos < len(exp) and (exp[pos].isdigit() or exp[pos] == '.'):
        ch += exp[pos]
        pos += 1
    return ch, pos - i


def handle_term(exp, i):
    """
    handles a single term in a math expression
    :param exp: string math expression
    :param i: index of term to handle
    :return: the term and its length in the expression, or None for error
    """
    ch = exp[i]
    if ch not in OPERATORS and not ch.isdigit() and ch not in ('.', '(', ')'):
        print("invalid expression:", ch)
        return None
    elif ch.isdigit() or ch == '.' or (ch == '-' and (i == 0 or exp[i - 1] in OPERATORS)):
        ch, length = construct_number(exp, i)
        try:
            ch = float(remove_minuses(ch))
        except ValueError:
            print(ch, "not a number")
            return None
        return ch, length
    else:
        return ch, 1


def get_expression():
    """
    receives a math expression and breaks it into individual terms
    :return: a list containing the terms of the given expression
    """
    infix = []
    i = 0
    exp = input("enter expression to calculate")
    exp = exp.replace(" ", "")
    while i < len(exp):
        ch = handle_term(exp, i)
        if ch is None:
            return ch
        infix.append(ch[0])
        i += ch[1]
    return infix


def turn_postfix(infix):
    stack = []
    postfix = []


def main():
    while True:
        infix = get_expression()
        if infix is None:
            continue


if __name__ == '__main__':
    main()
