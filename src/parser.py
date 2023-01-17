from .model.token import Token, TokenType
from .model.ast import (
    AddNode,
    SubtNode,
    MultNode,
    DivNode,
    PlusNode,
    MinusNode,
    NumNode,
    AST,
)
from .lexer import Lexer


class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        if len(tokens) == 0:
            raise RuntimeError("Empty token list")
        self.tokens = iter(tokens)
        self.curr_token = None
        self.ast = None
        self.next()

    def parse(self) -> AST:
        if self.ast == None:
            self.ast = self.generate_ast()
        return self.ast

    def next(self) -> None:
        try:
            self.curr_token = next(self.tokens)
        except StopIteration:
            self.curr_token = None

    def generate_ast(self) -> AST:
        if self.curr_token == None:
            raise RuntimeError("Start token is empty")

        result = self.expr()

        if self.curr_token != None:
            raise RuntimeError(
                f"Invalid syntax: token '{self.curr_token}' left after parsing"
            )

        return result

    # E -> T + T | T - T | T
    def expr(self) -> AST:
        result = self.term()
        while self.curr_token != None and self.curr_token.type in (
            TokenType.MINUS,
            TokenType.PLUS,
        ):
            if self.curr_token.type == TokenType.PLUS:
                self.next()
                result = AddNode(result, self.term())
            elif self.curr_token.type == TokenType.MINUS:
                self.next()
                result = SubtNode(result, self.term())
        return result

    # T -> F * F | F / F | F
    def term(self) -> AST:
        result = self.factor()
        while self.curr_token != None and self.curr_token.type in (
            TokenType.MULTIPLY,
            TokenType.DIVIDE,
        ):
            if self.curr_token.type == TokenType.MULTIPLY:
                self.next()
                result = MultNode(result, self.factor())
            elif self.curr_token.type == TokenType.DIVIDE:
                self.next()
                result = DivNode(result, self.factor())
        return result

    # F -> num | -F | +F | (E)
    def factor(self) -> AST:
        token = self.curr_token
        if token != None and token.type == TokenType.NUM:
            self.next()
            return NumNode(token.value)
        elif token != None and token.type == TokenType.PLUS:
            self.next()
            return PlusNode(self.factor())
        elif token != None and token.type == TokenType.MINUS:
            self.next()
            return MinusNode(self.factor())
        elif token != None and token.type == TokenType.LPAR:
            self.next()
            result = self.expr()
            if self.curr_token == None or self.curr_token.type != TokenType.RPAR:
                raise RuntimeError(
                    f"Syntax error: no matching RPAR token (found '{self.curr_token}')"
                )
            self.next()
            return result
        else:
            raise RuntimeError(
                f"Syntax error: unexpected token for factor rule (found '{self.curr_token}')"
            )


def main():
    while True:
        text = input("parser > ")
        lexer = Lexer(text)
        tokens = lexer.scan()
        parser = Parser(tokens)
        ast = parser.parse()

        print(f"\tinput: {text}")
        print(f"\ttokens: {tokens}")
        print(f"\tast: {ast}", end="\n\n")


if __name__ == "__main__":
    main()
