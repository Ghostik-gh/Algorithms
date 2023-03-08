"""
В единственной строке записано выражение в постфиксной
записи, содержащее цифры и операции +, -, *. Цифры и
операции разделяются пробелами.

! В конце строки может быть произвольное количество пробелов.

Необходимо вывести значение записанного выражения.
"""

operators = {
    '+': lambda m, n: n + m,
    '-': lambda m, n: n - m,
    '*': lambda m, n: n * m
}


def calculate(expr_postfix: str) -> int:
    stack: list[int] = list()
    for token in expr_postfix.split():
        if token.isnumeric():
            stack.append(int(token))
        else:
            result = operators[token](stack.pop(), stack.pop())
            stack.append(result)
    return stack.pop()


print(calculate(input()))
