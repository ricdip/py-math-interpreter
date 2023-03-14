include config.mk

.DEFAULT_GOAL := help

# help
.SILENT: help
.PHONY: help # display this help message
help:
	@grep -E '^.PHONY:.+#.+' Makefile | sed 's/.PHONY: //' | awk -F ' # ' '{printf "%-20s %s\n", $$1, $$2}'

# main
.PHONY: run_main # execute example
run_main:
	$(PYTHONMOD) $(MAIN)

.PHONY: run_lexer # execute Lexer
run_lexer:
	$(PYTHONMOD) $(LEXER)

.PHONY: run_parser # execute Parser
run_parser:
	$(PYTHONMOD) $(PARSER)

.PHONY: run_interpreter # execute Interpreter
run_interpreter:
	$(PYTHONMOD) $(INTERPRETER)

.PHONY: tests # execute all tests
tests:
	$(PYTHONTESTMOD) $(UNITTESTLEXER)
	$(PYTHONTESTMOD) $(UNITTESTPARSER)
	$(PYTHONTESTMOD) $(UNITTESTINTERPRETER)
	$(PYTHONTESTMOD) $(INTEGRATIONTESTALLMOD)

.PHONY: format # run Python Black formatter
format:
	fd --type f -e py | xargs $(FORMATTER)
