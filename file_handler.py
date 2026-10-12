"""Read expression files and write results while preserving separator lines."""
from pathlib import Path
from expression_evaluator import evaluate_expression


def is_separator(line):
    """Treat a line made of at least three hyphens as a separator."""
    return len(line.strip()) >= 3 and set(line.strip()) == {"-"}


def format_result(value):
    """Avoid unnecessary .0 for whole-number floating-point results."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def process_file(input_path="input.txt", output_path="output.txt"):
    """Evaluate each nonblank, nonseparator line and preserve separators."""
    input_file = Path(input_path)
    output_file = Path(output_path)

    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    output_lines = []
    errors = []

    for line_number, raw_line in enumerate(
        input_file.read_text(encoding="utf-8").splitlines(), start=1
    ):
        stripped = raw_line.strip()

        if not stripped:
            output_lines.append("")
        elif is_separator(stripped):
            output_lines.append(raw_line)
        else:
            try:
                result = evaluate_expression(stripped)
                output_lines.append(format_result(result))
            except (ValueError, ZeroDivisionError, IndexError) as exc:
                output_lines.append(f"ERROR: {exc}")
                errors.append((line_number, str(exc)))

    output_file.write_text(
        "\n".join(output_lines) + ("\n" if output_lines else ""),
        encoding="utf-8"
    )
    return errors
