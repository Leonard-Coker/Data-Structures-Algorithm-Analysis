"""Entry point for the stack-based expression evaluator."""
import argparse
from file_handler import process_file


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate arithmetic expressions in a text file using stacks."
    )
    parser.add_argument("-i", "--input", default="input.txt",
                        help="Input text file (default: input.txt)")
    parser.add_argument("-o", "--output", default="output.txt",
                        help="Output text file (default: output.txt)")
    args = parser.parse_args()

    try:
        errors = process_file(args.input, args.output)
    except (OSError, UnicodeError) as exc:
        print(f"File error: {exc}")
        raise SystemExit(1)

    print(f"Finished. Results written to {args.output}.")
    if errors:
        print(f"{len(errors)} expression(s) could not be evaluated:")
        for line_number, message in errors:
            print(f"  Line {line_number}: {message}")
        raise SystemExit(2)


if __name__ == "__main__":
    main()
