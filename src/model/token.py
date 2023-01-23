from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    ASTERISK = 3
    SLASH = 4
    LPAR = 5
    RPAR = 6


@dataclass
class Token:
    type: TokenType
    value: str

    def __repr__(self) -> str:
        return f"({self.type.name}, '{self.value}')"
