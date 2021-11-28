from sympy import *
from sympy.parsing.sympy_parser import parse_expr


def sol_equation(lhs, rhs):
    lhs = parse_expr(lhs)
    rhs = parse_expr(rhs)
    return solve(lhs - rhs)


def sol(expression):
    return parse_expr(expression)


def calculator(expression):
    try:
        if '=' in expression:
            # solve equation
            lhs = expression.split('=')[0]
            rhs = expression.split('=')[1]
            return sol_equation(lhs, rhs)
        else:
            return sol(expression)
    except IndexError:
        print('Please enter the expression to evaluate. Missing argument!!!')


print(calculator('3+4'))
