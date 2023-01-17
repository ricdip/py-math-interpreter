from dataclasses import dataclass
from typing import Union


@dataclass
class AddNode:
    left: "AST"
    right: "AST"

    def __repr__(self) -> str:
        return f"({self.left} + {self.right})"


@dataclass
class SubtNode:
    left: "AST"
    right: "AST"

    def __repr__(self) -> str:
        return f"({self.left} - {self.right})"


@dataclass
class MultNode:
    left: "AST"
    right: "AST"

    def __repr__(self) -> str:
        return f"({self.left} * {self.right})"


@dataclass
class DivNode:
    left: "AST"
    right: "AST"

    def __repr__(self) -> str:
        return f"({self.left} / {self.right})"


@dataclass
class PlusNode:
    data: "AST"

    def __repr__(self) -> str:
        return f"(+{self.data})"


@dataclass
class MinusNode:
    data: "AST"

    def __repr__(self) -> str:
        return f"(-{self.data})"


@dataclass
class NumNode:
    data: str

    def __repr__(self) -> str:
        return f"{self.data}"


AST = Union[AddNode, SubtNode, MultNode, DivNode, PlusNode, MinusNode, NumNode]
