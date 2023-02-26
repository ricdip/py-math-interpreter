# config
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

.DEFAULT_GOAL := help

# help
.SILENT: help
.PHONY: help # Display this help message
help:
	@grep -E '^.PHONY:.+#.+' Makefile | sed 's/.PHONY: //' | awk -F ' # ' '{printf "%-20s %s\n", $$1, $$2}'


# main
.PHONY: run_main # Execute example
run_main:
	$(PYTHONMOD) $(MAIN)

.PHONY: run_lexer # Execute Lexer
run_lexer:
	$(PYTHONMOD) $(LEXER)

.PHONY: run_parser # Execute Parser
run_parser:
	$(PYTHONMOD) $(PARSER)

.PHONY: run_interpreter # Execute Interpreter
run_interpreter:
	$(PYTHONMOD) $(INTERPRETER)

.PHONY: tests # Execute all tests
tests:
	$(PYTHONTESTMOD) $(UNITTESTLEXER)
	$(PYTHONTESTMOD) $(UNITTESTPARSER)
	$(PYTHONTESTMOD) $(UNITTESTINTERPRETER)
	$(PYTHONTESTMOD) $(INTEGRATIONTESTALLMOD)

.PHONY: format # Run Python Black formatter
format:
	fd --type f -e py | xargs black
