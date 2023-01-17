import unittest
from ...model.token import Token, TokenType
from ...model.ast import (
    AddNode,
    SubtNode,
    MultNode,
    DivNode,
    PlusNode,
    MinusNode,
    NumNode,
)
from ...parser import Parser


class TestParser(unittest.TestCase):
    def test_empty(self):
        tokens = []
        with self.assertRaises(Exception):
            Parser(tokens).parse()

    def test_add(self):
        tokens = [
            Token(TokenType.NUM, "1"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUM, "2"),
        ]
        ast = Parser(tokens).parse()
        result = AddNode(NumNode("1"), NumNode("2"))
        self.assertEqual(ast, result)

    def test_subtract(self):
        tokens = [
            Token(TokenType.NUM, "1"),
            Token(TokenType.MINUS, "-"),
            Token(TokenType.NUM, "2"),
        ]
        ast = Parser(tokens).parse()
        result = SubtNode(NumNode("1"), NumNode("2"))
        self.assertEqual(ast, result)

    def test_multiply(self):
        tokens = [
            Token(TokenType.NUM, "1"),
            Token(TokenType.MULTIPLY, "*"),
            Token(TokenType.NUM, "2"),
        ]
        ast = Parser(tokens).parse()
        result = MultNode(NumNode("1"), NumNode("2"))
        self.assertEqual(ast, result)

    def test_divide(self):
        tokens = [
            Token(TokenType.NUM, "1"),
            Token(TokenType.DIVIDE, "/"),
            Token(TokenType.NUM, "2"),
        ]
        ast = Parser(tokens).parse()
        result = DivNode(NumNode("1"), NumNode("2"))
        self.assertEqual(ast, result)

    def test_plus(self):
        tokens = [
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUM, "1"),
        ]
        ast = Parser(tokens).parse()
        result = PlusNode(NumNode("1"))
        self.assertEqual(ast, result)

    def test_minus(self):
        tokens = [
            Token(TokenType.MINUS, "-"),
            Token(TokenType.NUM, "1"),
        ]
        ast = Parser(tokens).parse()
        result = MinusNode(NumNode("1"))
        self.assertEqual(ast, result)

    def test_number(self):
        tokens = [
            Token(TokenType.NUM, "1"),
        ]
        ast = Parser(tokens).parse()
        result = NumNode("1")
        self.assertEqual(ast, result)

    def test_wrong_expr(self):
        tokens = [
            Token(TokenType.NUM, "1"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUM, "2"),
            Token(TokenType.NUM, "3"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUM, "5"),
        ]
        with self.assertRaises(Exception):
            Parser(tokens).parse()

    def test_wrong_pars_1(self):
        tokens = [
            Token(TokenType.NUM, "1"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.LPAR, "("),
            Token(TokenType.NUM, "2"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUM, "3"),
            Token(TokenType.RPAR, ")"),
            Token(TokenType.RPAR, ")"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUM, "5"),
        ]
        with self.assertRaises(Exception):
            Parser(tokens).parse()

    def test_wrong_pars_2(self):
        tokens = [
            Token(TokenType.NUM, "1"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.LPAR, "("),
            Token(TokenType.NUM, "2"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUM, "3"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUM, "5"),
        ]
        with self.assertRaises(Exception):
            Parser(tokens).parse()

    def test_wrong_pars_3(self):
        tokens = [
            Token(TokenType.NUM, "1"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.RPAR, ")"),
            Token(TokenType.NUM, "2"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUM, "3"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUM, "5"),
        ]
        with self.assertRaises(Exception):
            Parser(tokens).parse()

    def test_all(self):
        # expr = 1 - 2 * 3 / 4 + (1.5 + 2.5 * 4)
        tokens = [
            Token(TokenType.NUM, "1"),
            Token(TokenType.MINUS, "-"),
            Token(TokenType.NUM, "2"),
            Token(TokenType.MULTIPLY, "*"),
            Token(TokenType.NUM, "3"),
            Token(TokenType.DIVIDE, "/"),
            Token(TokenType.NUM, "4"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.LPAR, "("),
            Token(TokenType.NUM, "1.5"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUM, "2.5"),
            Token(TokenType.MULTIPLY, "*"),
            Token(TokenType.NUM, "4"),
            Token(TokenType.RPAR, ")"),
        ]
        # ast = ((1 - ((2 * 3) / 4)) + (1.5 + (2.5 * 4)))
        ast = Parser(tokens).parse()
        result = AddNode(
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
        self.assertEqual(ast, result)
