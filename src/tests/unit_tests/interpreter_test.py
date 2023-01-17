import unittest
from ...model.ast import (
    AddNode,
    SubtNode,
    MultNode,
    DivNode,
    PlusNode,
    MinusNode,
    NumNode,
)
from ...interpreter import Interpreter


class TestInterpreter(unittest.TestCase):
    def test_empty(self):
        ast = None
        with self.assertRaises(Exception):
            Interpreter(ast).interpret()  # type: ignore

    def test_add(self):
        ast = AddNode(NumNode("1"), NumNode("2"))
        output = Interpreter(ast).interpret().data
        result = 3
        self.assertEqual(output, result)

    def test_subtract(self):
        ast = SubtNode(NumNode("1"), NumNode("2"))
        output = Interpreter(ast).interpret().data
        result = -1
        self.assertEqual(output, result)

    def test_multiply(self):
        ast = MultNode(NumNode("2"), NumNode("3"))
        output = Interpreter(ast).interpret().data
        result = 6
        self.assertEqual(output, result)

    def test_divide(self):
        ast = DivNode(NumNode("6"), NumNode("2"))
        output = Interpreter(ast).interpret().data
        result = 3
        self.assertEqual(output, result)

    def test_divide_by_0(self):
        ast = DivNode(NumNode("2"), NumNode("0"))
        with self.assertRaises(Exception):
            Interpreter(ast).interpret()

    def test_plus(self):
        ast = PlusNode(NumNode("1"))
        output = Interpreter(ast).interpret().data
        result = 1
        self.assertEqual(output, result)

    def test_minus(self):
        ast = MinusNode(NumNode("1"))
        output = Interpreter(ast).interpret().data
        result = -1
        self.assertEqual(output, result)

    def test_number(self):
        ast = NumNode("1")
        output = Interpreter(ast).interpret().data
        result = 1
        self.assertEqual(output, result)

    def test_all(self):
        # expr = 1 - 2 * 3 / 4 + (1.5 + 2.5 * 4) = 11
        # ast = ((1 - ((2 * 3) / 4)) + (1.5 + (2.5 * 4)))
        ast = AddNode(
            SubtNode(
                NumNode("1"),
                DivNode(
                    MultNode(
                        NumNode("2"),
                        NumNode("3"),
                    ),
                    NumNode("4"),
                ),
            ),
            AddNode(
                NumNode("1.5"),
                MultNode(
                    NumNode("2.5"),
                    NumNode("4"),
                ),
            ),
        )
        output = Interpreter(ast).interpret().data
        result = 11.0
        self.assertAlmostEqual(output, result)
