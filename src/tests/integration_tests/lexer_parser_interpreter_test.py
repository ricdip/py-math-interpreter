import unittest
from ...lexer import Lexer
from ...parser import Parser
from ...interpreter import Interpreter


class TestLexerParserInterpreter(unittest.TestCase):
    def test_empty(self):
        text = ""
        with self.assertRaises(Exception):
            tokens = Lexer(text).scan()
            ast = Parser(tokens).parse()
            Interpreter(ast).interpret()

    def test_whitespaces(self):
        text = "   \n\n  \t "
        with self.assertRaises(Exception):
            tokens = Lexer(text).scan()
            ast = Parser(tokens).parse()
            Interpreter(ast).interpret()

    def test_add(self):
        text = "1+2+3+4"
        tokens = Lexer(text).scan()
        ast = Parser(tokens).parse()
        output = Interpreter(ast).interpret().value
        result = 10
        self.assertEqual(output, result)

    def test_subtract(self):
        text = "1-2-3-4"
        tokens = Lexer(text).scan()
        ast = Parser(tokens).parse()
        output = Interpreter(ast).interpret().value
        result = -8
        self.assertEqual(output, result)

    def test_multiply(self):
        text = "1*2*3*4"
        tokens = Lexer(text).scan()
        ast = Parser(tokens).parse()
        output = Interpreter(ast).interpret().value
        result = 24
        self.assertEqual(output, result)

    def test_divide(self):
        text = "1/2/3/4"
        tokens = Lexer(text).scan()
        ast = Parser(tokens).parse()
        output = Interpreter(ast).interpret().value
        result = 0.04166
        self.assertAlmostEqual(output, result, 4)

    def test_plus(self):
        text = "+++++2"
        tokens = Lexer(text).scan()
        ast = Parser(tokens).parse()
        output = Interpreter(ast).interpret().value
        result = 2
        self.assertEqual(output, result)

    def test_minus_1(self):
        text = "-----2"
        tokens = Lexer(text).scan()
        ast = Parser(tokens).parse()
        output = Interpreter(ast).interpret().value
        result = -2
        self.assertEqual(output, result)

    def test_minus_2(self):
        text = "----2"
        tokens = Lexer(text).scan()
        ast = Parser(tokens).parse()
        output = Interpreter(ast).interpret().value
        result = 2
        self.assertEqual(output, result)

    def test_number(self):
        text = "2"
        tokens = Lexer(text).scan()
        ast = Parser(tokens).parse()
        output = Interpreter(ast).interpret().value
        result = 2
        self.assertEqual(output, result)

    def test_all(self):
        # expr = 1 - 2 * 3 / 4 + (1.5 + 2.5 * 4) = 11.0
        text = "1 - 2 * 3 / 4 + (1.5 + 2.5 * 4)"
        tokens = Lexer(text).scan()
        ast = Parser(tokens).parse()
        output = Interpreter(ast).interpret().value
        result = 11.0
        self.assertAlmostEqual(output, result)
