PYTHON = python
PYTHONMOD = $(PYTHON) -m
PYTHONTESTMOD = $(PYTHONMOD) unittest

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


.PHONY: run_main
run_main:
	$(PYTHONMOD) $(MAIN)

.PHONY: run_lexer
run_lexer:
	$(PYTHONMOD) $(LEXER)

.PHONY: run_parser
run_parser:
	$(PYTHONMOD) $(PARSER)

.PHONY: run_interpreter
run_interpreter:
	$(PYTHONMOD) $(INTERPRETER)

.PHONY: tests
tests:
	$(PYTHONTESTMOD) $(UNITTESTLEXER)
	$(PYTHONTESTMOD) $(UNITTESTPARSER)
	$(PYTHONTESTMOD) $(UNITTESTINTERPRETER)
	$(PYTHONTESTMOD) $(INTEGRATIONTESTALLMOD)

.PHONY: format
format:
	fd --type f -e py | xargs black

