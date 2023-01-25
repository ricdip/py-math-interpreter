from dataclasses import dataclass
from typing import Union


@dataclass
class AddNode:
    left: "AST"
    right: "AST"

    def __repr__(self) -> str:
        return f"({self.left} + {self.right})"


@dataclass
class SubtractNode:
    left: "AST"
    right: "AST"

    def __repr__(self) -> str:
        return f"({self.left} - {self.right})"


@dataclass
class MultiplyNode:
    left: "AST"
    right: "AST"

    def __repr__(self) -> str:
        return f"({self.left} * {self.right})"


@dataclass
class DivideNode:
    left: "AST"
    right: "AST"

    def __repr__(self) -> str:
        return f"({self.left} / {self.right})"


@dataclass
class PlusNode:
    value: "AST"

    def __repr__(self) -> str:
        return f"(+{self.value})"


@dataclass
class MinusNode:
    value: "AST"

    def __repr__(self) -> str:
        return f"(-{self.value})"


@dataclass
class NumberNode:
    value: str

    def __repr__(self) -> str:
        return f"{self.value}"


AST = Union[
    AddNode, SubtractNode, MultiplyNode, DivideNode, PlusNode, MinusNode, NumberNode
]
