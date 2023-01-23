import unittest
from ...model.ast import (
    AddNode,
    SubtractNode,
    MultiplyNode,
    DivideNode,
    PlusNode,
    MinusNode,
    NumberNode,
)
from ...interpreter import Interpreter


class TestInterpreter(unittest.TestCase):
    def test_empty(self):
        ast = None
        with self.assertRaises(Exception):
            Interpreter(ast).interpret()  # type: ignore

    def test_add(self):
        ast = AddNode(NumberNode("1"), NumberNode("2"))
        output = Interpreter(ast).interpret().value
        result = 3
        self.assertEqual(output, result)

    def test_subtract(self):
        ast = SubtractNode(NumberNode("1"), NumberNode("2"))
        output = Interpreter(ast).interpret().value
        result = -1
        self.assertEqual(output, result)

    def test_multiply(self):
        ast = MultiplyNode(NumberNode("2"), NumberNode("3"))
        output = Interpreter(ast).interpret().value
        result = 6
        self.assertEqual(output, result)

    def test_divide(self):
        ast = DivideNode(NumberNode("6"), NumberNode("2"))
        output = Interpreter(ast).interpret().value
        result = 3
        self.assertEqual(output, result)

    def test_divide_by_0(self):
        ast = DivideNode(NumberNode("2"), NumberNode("0"))
        with self.assertRaises(Exception):
            Interpreter(ast).interpret()

    def test_plus(self):
        ast = PlusNode(NumberNode("1"))
        output = Interpreter(ast).interpret().value
        result = 1
        self.assertEqual(output, result)

    def test_minus(self):
        ast = MinusNode(NumberNode("1"))
        output = Interpreter(ast).interpret().value
        result = -1
        self.assertEqual(output, result)

    def test_number(self):
        ast = NumberNode("1")
        output = Interpreter(ast).interpret().value
        result = 1
        self.assertEqual(output, result)

    def test_all(self):
        # expr = 1 - 2 * 3 / 4 + (1.5 + 2.5 * 4) = 11
        # ast = ((1 - ((2 * 3) / 4)) + (1.5 + (2.5 * 4)))
        ast = AddNode(
            SubtractNode(
                NumberNode("1"),
                DivideNode(
                    MultiplyNode(
                        NumberNode("2"),
                        NumberNode("3"),
                    ),
                    NumberNode("4"),
                ),
            ),
            AddNode(
                NumberNode("1.5"),
                MultiplyNode(
                    NumberNode("2.5"),
                    NumberNode("4"),
                ),
            ),
        )
        output = Interpreter(ast).interpret().value
        result = 11.0
        self.assertAlmostEqual(output, result)
