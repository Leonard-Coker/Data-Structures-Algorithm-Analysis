import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from stack import Stack
from expression_evaluator import evaluate_expression
from file_handler import process_file


class TestStack(unittest.TestCase):
    def test_push_peek_pop(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        self.assertEqual(stack.peek(), 20)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)
        self.assertTrue(stack.is_empty())

    def test_empty_pop_raises(self):
        with self.assertRaises(IndexError):
            Stack().pop()


class TestExpressionEvaluator(unittest.TestCase):
    def test_precedence(self):
        self.assertEqual(evaluate_expression("3 + 5 * 2"), 13)

    def test_parentheses(self):
        self.assertEqual(evaluate_expression("(8 / 4) + 7 * 2"), 16)

    def test_nested_parentheses(self):
        self.assertEqual(evaluate_expression("2 * (3 + (4 * 2))"), 22)

    def test_subtraction_and_negative_result(self):
        self.assertEqual(evaluate_expression("10 - (2 + 3) * 4"), -10)

    def test_decimal(self):
        self.assertAlmostEqual(evaluate_expression("2.5 * 2"), 5)

    def test_unary_minus(self):
        self.assertEqual(evaluate_expression("-5 + 2"), -3)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            evaluate_expression("5 / 0")

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            evaluate_expression("5 + * 2")


class TestFileProcessing(unittest.TestCase):
    def test_separators_preserved(self):
        test_dir = Path(__file__).parent / "temp"
        test_dir.mkdir(exist_ok=True)
        source = test_dir / "input.txt"
        target = test_dir / "output.txt"
        try:
            source.write_text("3 + 5 * 2\n------\n8 / 2\n", encoding="utf-8")
            errors = process_file(source, target)
            self.assertEqual(errors, [])
            self.assertEqual(target.read_text(encoding="utf-8"), "13\n------\n4\n")
        finally:
            for path in (source, target):
                if path.exists():
                    path.unlink()
            if test_dir.exists():
                test_dir.rmdir()


if __name__ == "__main__":
    unittest.main()
