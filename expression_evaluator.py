"""Evaluate arithmetic expressions using operand and operator stacks."""
from stack import Stack
from tokenizer import tokenize


PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2}


def _apply_operator(operands, operator):
    if operands.size() < 2:
        raise ValueError("Operator is missing an operand.")

    right = operands.pop()
    left = operands.pop()

    if operator == "+":
        result = left + right
    elif operator == "-":
        result = left - right
    elif operator == "*":
        result = left * right
    elif operator == "/":
        if right == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        result = left / right
    else:
        raise ValueError(f"Unsupported operator: {operator}")

    operands.push(result)


def evaluate_expression(expression):
    """Evaluate +, -, *, / and parentheses without using eval()."""
    tokens = tokenize(expression)
    operands = Stack()
    operators = Stack()
    expecting_operand = True

    for token in tokens:
        if isinstance(token, (int, float)):
            if not expecting_operand:
                raise ValueError("Two numbers appear without an operator.")
            operands.push(token)
            expecting_operand = False

        elif token == "(":
            if not expecting_operand:
                raise ValueError("Missing operator before '('.")
            operators.push(token)
            expecting_operand = True

        elif token == ")":
            if expecting_operand:
                raise ValueError("Unexpected ')' or missing operand.")
            while not operators.is_empty() and operators.peek() != "(":
                _apply_operator(operands, operators.pop())
            if operators.is_empty():
                raise ValueError("Mismatched parentheses: missing '('.")
            operators.pop()
            expecting_operand = False

        else:
            # Support unary + and - by treating them as 0 +/- value.
            if expecting_operand:
                if token in ("+", "-"):
                    operands.push(0)
                else:
                    raise ValueError(f"Unexpected operator {token!r}.")
            while (not operators.is_empty()
                   and operators.peek() != "("
                   and PRECEDENCE[operators.peek()] >= PRECEDENCE[token]):
                _apply_operator(operands, operators.pop())
            operators.push(token)
            expecting_operand = True

    if expecting_operand:
        raise ValueError("Expression ends before an operand.")

    while not operators.is_empty():
        operator = operators.pop()
        if operator == "(":
            raise ValueError("Mismatched parentheses: missing ')'.")
        _apply_operator(operands, operator)

    if operands.size() != 1:
        raise ValueError("Expression could not be evaluated.")
    return operands.pop()
