"""Convert arithmetic expression text into numbers, operators, and parentheses."""
import re


NUMBER_PATTERN = re.compile(r"(?:\d+(?:\.\d*)?|\.\d+)")


def tokenize(expression):
    """Return tokens from an expression; reject unsupported or malformed characters."""
    tokens = []
    i = 0
    while i < len(expression):
        char = expression[i]

        if char.isspace():
            i += 1
            continue

        number_match = NUMBER_PATTERN.match(expression, i)
        if number_match:
            tokens.append(float(number_match.group()) if "." in number_match.group()
                          else int(number_match.group()))
            i = number_match.end()
            continue

        if char in "+-*/()":
            tokens.append(char)
            i += 1
            continue

        raise ValueError(f"Unsupported character {char!r} in expression.")

    if not tokens:
        raise ValueError("Expression is empty.")
    return tokens
