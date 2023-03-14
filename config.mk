PYTHON = python
PYTHONMOD = $(PYTHON) -m
PYTHONTESTMOD = $(PYTHONMOD) unittest
FORMATTER = black

BASE = src
BASETEST = $(BASE).tests
MAIN = $(BASE).main
LEXER = $(BASE).lexer
PARSER = $(BASE).parser
INTERPRETER = $(BASE).interpreter

UNITTEST = $(BASETEST).unit_tests
UNITTESTLEXER = $(UNITTEST).lexer_test
UNITTESTPARSER = $(UNITTEST).parser_test
UNITTESTINTERPRETER = $(UNITTEST).interpreter_test

INTEGRATIONTEST = $(BASETEST).integration_tests
INTEGRATIONTESTALLMOD = $(BASETEST).integration_tests.lexer_parser_interpreter_test
