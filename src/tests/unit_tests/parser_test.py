import unittest
from ...model.token import Token, TokenType
from ...model.ast import (
    AddNode,
    SubtractNode,
    MultiplyNode,
    DivideNode,
    PlusNode,
    MinusNode,
    NumberNode,
)
from ...parser import Parser


class TestParser(unittest.TestCase):
    def test_empty(self):
        tokens = []
        with self.assertRaises(Exception):
            Parser(tokens).parse()

    def test_add(self):
        tokens = [
            Token(TokenType.NUMBER, "1"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUMBER, "2"),
        ]
        ast = Parser(tokens).parse()
        result = AddNode(NumberNode("1"), NumberNode("2"))
        self.assertEqual(ast, result)

    def test_subtract(self):
        tokens = [
            Token(TokenType.NUMBER, "1"),
            Token(TokenType.MINUS, "-"),
            Token(TokenType.NUMBER, "2"),
        ]
        ast = Parser(tokens).parse()
        result = SubtractNode(NumberNode("1"), NumberNode("2"))
        self.assertEqual(ast, result)

    def test_multiply(self):
        tokens = [
            Token(TokenType.NUMBER, "1"),
            Token(TokenType.ASTERISK, "*"),
            Token(TokenType.NUMBER, "2"),
        ]
        ast = Parser(tokens).parse()
        result = MultiplyNode(NumberNode("1"), NumberNode("2"))
        self.assertEqual(ast, result)

    def test_divide(self):
        tokens = [
            Token(TokenType.NUMBER, "1"),
            Token(TokenType.SLASH, "/"),
            Token(TokenType.NUMBER, "2"),
        ]
        ast = Parser(tokens).parse()
        result = DivideNode(NumberNode("1"), NumberNode("2"))
        self.assertEqual(ast, result)

    def test_plus(self):
        tokens = [
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUMBER, "1"),
        ]
        ast = Parser(tokens).parse()
        result = PlusNode(NumberNode("1"))
        self.assertEqual(ast, result)

    def test_minus(self):
        tokens = [
            Token(TokenType.MINUS, "-"),
            Token(TokenType.NUMBER, "1"),
        ]
        ast = Parser(tokens).parse()
        result = MinusNode(NumberNode("1"))
        self.assertEqual(ast, result)

    def test_number(self):
        tokens = [
            Token(TokenType.NUMBER, "1"),
        ]
        ast = Parser(tokens).parse()
        result = NumberNode("1")
        self.assertEqual(ast, result)

    def test_wrong_expr(self):
        tokens = [
            Token(TokenType.NUMBER, "1"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUMBER, "2"),
            Token(TokenType.NUMBER, "3"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUMBER, "5"),
        ]
        with self.assertRaises(Exception):
            Parser(tokens).parse()

    def test_wrong_pars_1(self):
        tokens = [
            Token(TokenType.NUMBER, "1"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.LPAR, "("),
            Token(TokenType.NUMBER, "2"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUMBER, "3"),
            Token(TokenType.RPAR, ")"),
            Token(TokenType.RPAR, ")"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUMBER, "5"),
        ]
        with self.assertRaises(Exception):
            Parser(tokens).parse()

    def test_wrong_pars_2(self):
        tokens = [
            Token(TokenType.NUMBER, "1"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.LPAR, "("),
            Token(TokenType.NUMBER, "2"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUMBER, "3"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUMBER, "5"),
        ]
        with self.assertRaises(Exception):
            Parser(tokens).parse()

    def test_wrong_pars_3(self):
        tokens = [
            Token(TokenType.NUMBER, "1"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.RPAR, ")"),
            Token(TokenType.NUMBER, "2"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUMBER, "3"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUMBER, "5"),
        ]
        with self.assertRaises(Exception):
            Parser(tokens).parse()

    def test_all(self):
        # expr = 1 - 2 * 3 / 4 + (1.5 + 2.5 * 4)
        tokens = [
            Token(TokenType.NUMBER, "1"),
            Token(TokenType.MINUS, "-"),
            Token(TokenType.NUMBER, "2"),
            Token(TokenType.ASTERISK, "*"),
            Token(TokenType.NUMBER, "3"),
            Token(TokenType.SLASH, "/"),
            Token(TokenType.NUMBER, "4"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.LPAR, "("),
            Token(TokenType.NUMBER, "1.5"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUMBER, "2.5"),
            Token(TokenType.ASTERISK, "*"),
            Token(TokenType.NUMBER, "4"),
            Token(TokenType.RPAR, ")"),
        ]
        # ast = ((1 - ((2 * 3) / 4)) + (1.5 + (2.5 * 4)))
        ast = Parser(tokens).parse()
        result = AddNode(
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
        self.assertEqual(ast, result)
