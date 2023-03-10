from .model.characters import (
    WHITESPACES,
    DIGITS,
    POINT,
    PLUS,
    MINUS,
    ASTERISK,
    SLASH,
    LPAR,
    RPAR,
)
from .model.token import Token, TokenType


class Lexer:
    def __init__(self, text: str) -> None:
        if len(text) == 0:
            raise RuntimeError("Empty input text")
        self.text = iter(text)
        self.curr_char = None
        self.tokens = []
        self.next()

    def scan(self) -> list[Token]:
        if len(self.tokens) == 0:
            self.generate_tokens()
        return self.tokens

    def next(self) -> None:
        try:
            self.curr_char = next(self.text)
        except StopIteration:
            self.curr_char = None

    def generate_tokens(self) -> None:
        while self.curr_char != None:
            if self.curr_char in WHITESPACES:
                self.next()
            elif self.curr_char in DIGITS:
                self.tokens.append(self.generate_number())
            elif self.curr_char in PLUS:
                self.tokens.append(self.generate_plus())
            elif self.curr_char in MINUS:
                self.tokens.append(self.generate_minus())
            elif self.curr_char in ASTERISK:
                self.tokens.append(self.generate_asterisk())
            elif self.curr_char in SLASH:
                self.tokens.append(self.generate_slash())
            elif self.curr_char in LPAR:
                self.tokens.append(self.generate_lpar())
            elif self.curr_char in RPAR:
                self.tokens.append(self.generate_rpar())
            else:
                raise RuntimeError(f"Illegal character '{self.curr_char}'")

    def generate_number(self) -> Token:
        points_counter = 0
        integer_str = ""
        while self.curr_char != None and (
            self.curr_char in DIGITS or self.curr_char in POINT
        ):
            if self.curr_char in POINT:
                points_counter += 1
            integer_str += self.curr_char
            self.next()

        if points_counter > 1:
            raise RuntimeError(f"Illegal number '{integer_str}'")

        return Token(TokenType.NUMBER, integer_str)

    def generate_plus(self) -> Token:
        self.next()
        return Token(TokenType.PLUS, PLUS)

    def generate_minus(self) -> Token:
        self.next()
        return Token(TokenType.MINUS, MINUS)

    def generate_asterisk(self) -> Token:
        self.next()
        return Token(TokenType.ASTERISK, ASTERISK)

    def generate_slash(self) -> Token:
        self.next()
        return Token(TokenType.SLASH, SLASH)

    def generate_lpar(self) -> Token:
        self.next()
        return Token(TokenType.LPAR, LPAR)

    def generate_rpar(self) -> Token:
        self.next()
        return Token(TokenType.RPAR, RPAR)


def main():
    while True:
        text = input("lexer > ")
        lexer = Lexer(text)
        tokens = lexer.scan()

        print(f"\tinput: {text}")
        print(f"\ttokens: {tokens}", end="\n\n")


if __name__ == "__main__":
    main()
