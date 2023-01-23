from typing import cast
import math
from .model.characters import POINT
from .model.ast import (
    AST,
    AddNode,
    DivideNode,
    MinusNode,
    MultiplyNode,
    NumberNode,
    PlusNode,
    SubtractNode,
)
from .model.values import NumberValue
from .lexer import Lexer
from .parser import Parser


class Interpreter:
    def __init__(self, ast: AST):
        if ast == None:
            raise RuntimeError("AST is None")
        self.init_ast = ast
        self.result = None

    def interpret(self) -> NumberValue:
        if self.result == None:
            self.result = self.evaluate(self.init_ast)
        return self.result

    def evaluate(self, ast: AST) -> NumberValue:
        if type(ast) == AddNode:
            return self.interpret_add_node(cast(AddNode, ast))
        elif type(ast) == SubtractNode:
            return self.interpret_subt_node(cast(SubtractNode, ast))
        elif type(ast) == MultiplyNode:
            return self.interpret_mult_node(cast(MultiplyNode, ast))
        elif type(ast) == DivideNode:
            return self.interpret_div_node(cast(DivideNode, ast))
        elif type(ast) == PlusNode:
            return self.interpret_plus_node(cast(PlusNode, ast))
        elif type(ast) == MinusNode:
            return self.interpret_minus_node(cast(MinusNode, ast))
        elif type(ast) == NumberNode:
            return self.interpret_num_node(cast(NumberNode, ast))
        else:
            raise RuntimeError("Evaluation error: Illegal AST node")

    def interpret_add_node(self, node: AddNode) -> NumberValue:
        lhs = self.evaluate(node.left).value
        rhs = self.evaluate(node.right).value
        return NumberValue(lhs + rhs)

    def interpret_subt_node(self, node: SubtractNode) -> NumberValue:
        lhs = self.evaluate(node.left).value
        rhs = self.evaluate(node.right).value
        return NumberValue(lhs - rhs)

    def interpret_mult_node(self, node: MultiplyNode) -> NumberValue:
        lhs = self.evaluate(node.left).value
        rhs = self.evaluate(node.right).value
        return NumberValue(lhs * rhs)

    def interpret_div_node(self, node: DivideNode) -> NumberValue:
        lhs = self.evaluate(node.left).value
        rhs = self.evaluate(node.right).value
        # more reliable way to check if rhs == 0.0
        if math.isclose(rhs, 0.0):
            raise ValueError(f"Division by 0 detected: {lhs} / {rhs}")
        return NumberValue(lhs / rhs)

    def interpret_plus_node(self, node: PlusNode) -> NumberValue:
        rhs = self.evaluate(node.value).value
        return NumberValue(rhs)

    def interpret_minus_node(self, node: MinusNode) -> NumberValue:
        rhs = self.evaluate(node.value).value
        return NumberValue(-rhs)

    def interpret_num_node(self, node: NumberNode) -> NumberValue:
        number = node.value
        is_float = False

        if POINT in number:
            is_float = True

        # convert number in int or float
        if is_float:
            return NumberValue(float(number))
        else:
            return NumberValue(int(number))


def main():
    while True:
        text = input("interpreter > ")
        lexer = Lexer(text)
        tokens = lexer.scan()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter(ast)
        output = interpreter.interpret()

        print(f"\tinput: {text}")
        print(f"\ttokens: {tokens}")
        print(f"\tast: {ast}")
        print(f"\toutput: {output}", end="\n\n")


if __name__ == "__main__":
    main()
