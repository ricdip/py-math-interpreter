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
            Token(TokenType.NUMBER, "123"),
            Token(TokenType.NUMBER, "456"),
            Token(TokenType.NUMBER, "7889"),
            Token(TokenType.NUMBER, "0"),
            Token(TokenType.NUMBER, "11.5"),
            Token(TokenType.NUMBER, "122.65"),
            Token(TokenType.NUMBER, "110.5"),
        ]

        self.assertEqual(tokens, result)

    def test_operations(self):
        text = "+-/*"
        tokens = Lexer(text).scan()
        result = [
            Token(TokenType.PLUS, "+"),
            Token(TokenType.MINUS, "-"),
            Token(TokenType.SLASH, "/"),
            Token(TokenType.ASTERISK, "*"),
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
            Token(TokenType.NUMBER, "1"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUMBER, "2"),
            Token(TokenType.RPAR, ")"),
            Token(TokenType.ASTERISK, "*"),
            Token(TokenType.NUMBER, "4"),
            Token(TokenType.SLASH, "/"),
            Token(TokenType.NUMBER, "5.6"),
            Token(TokenType.MINUS, "-"),
            Token(TokenType.NUMBER, "2"),
        ]

        self.assertEqual(tokens, result)
