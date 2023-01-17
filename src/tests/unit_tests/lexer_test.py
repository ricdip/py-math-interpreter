import unittest
from ...lexer import Lexer
from ...model.token import Token, TokenType


class TestLexer(unittest.TestCase):
    def test_empty(self):
        text = ""
        with self.assertRaises(Exception):
            Lexer(text).scan()

    def test_whitespaces(self):
        text = "     \n\n \t\n  \t "
        tokens = Lexer(text).scan()
        result = []
        self.assertEqual(tokens, result)

    def test_numbers(self):
        text = "123 456 7889 0 11.5 122.65 110.5"
        tokens = Lexer(text).scan()
        result = [
            Token(TokenType.NUM, "123"),
            Token(TokenType.NUM, "456"),
            Token(TokenType.NUM, "7889"),
            Token(TokenType.NUM, "0"),
            Token(TokenType.NUM, "11.5"),
            Token(TokenType.NUM, "122.65"),
            Token(TokenType.NUM, "110.5"),
        ]

        self.assertEqual(tokens, result)

    def test_operations(self):
        text = "+-/*"
        tokens = Lexer(text).scan()
        result = [
            Token(TokenType.PLUS, "+"),
            Token(TokenType.MINUS, "-"),
            Token(TokenType.DIVIDE, "/"),
            Token(TokenType.MULTIPLY, "*"),
        ]

        self.assertEqual(tokens, result)

    def test_paren(self):
        text = "()"
        tokens = Lexer(text).scan()
        result = [
            Token(TokenType.LPAR, "("),
            Token(TokenType.RPAR, ")"),
        ]

        self.assertEqual(tokens, result)

    def test_wrong_characters(self):
        text = "?$!"
        with self.assertRaises(Exception):
            Lexer(text).scan()

    def test_all(self):
        text = "(1 + 2) * 4 / 5.6 - 2 \n\n\t "
        tokens = Lexer(text).scan()
        result = [
            Token(TokenType.LPAR, "("),
            Token(TokenType.NUM, "1"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUM, "2"),
            Token(TokenType.RPAR, ")"),
            Token(TokenType.MULTIPLY, "*"),
            Token(TokenType.NUM, "4"),
            Token(TokenType.DIVIDE, "/"),
            Token(TokenType.NUM, "5.6"),
            Token(TokenType.MINUS, "-"),
            Token(TokenType.NUM, "2"),
        ]

        self.assertEqual(tokens, result)
