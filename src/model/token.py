from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):
    NUM = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    LPAR = 5
    RPAR = 6


@dataclass
class Token:
    type: TokenType
    value: str

    def __repr__(self) -> str:
        return f"({self.type.name}, '{self.value}')"
