from typing import cast
import math
from .model.characters import POINT
from .model.ast import (
    AST,
    AddNode,
    DivNode,
    MinusNode,
    MultNode,
    NumNode,
    PlusNode,
    SubtNode,
)
from .model.values import NumValue
from .lexer import Lexer
from .parser import Parser


class Interpreter:
    def __init__(self, ast: AST):
        if ast == None:
            raise RuntimeError("AST is None")
        self.init_ast = ast
        self.result = None

    def interpret(self) -> NumValue:
        if self.result == None:
            self.result = self.evaluate(self.init_ast)
        return self.result

    def evaluate(self, ast: AST) -> NumValue:
        if type(ast) == AddNode:
            return self.interpret_add_node(cast(AddNode, ast))
        elif type(ast) == SubtNode:
            return self.interpret_subt_node(cast(SubtNode, ast))
        elif type(ast) == MultNode:
            return self.interpret_mult_node(cast(MultNode, ast))
        elif type(ast) == DivNode:
            return self.interpret_div_node(cast(DivNode, ast))
        elif type(ast) == PlusNode:
            return self.interpret_plus_node(cast(PlusNode, ast))
        elif type(ast) == MinusNode:
            return self.interpret_minus_node(cast(MinusNode, ast))
        elif type(ast) == NumNode:
            return self.interpret_num_node(cast(NumNode, ast))
        else:
            raise RuntimeError("Evaluation error: Illegal AST node")

    def interpret_add_node(self, node: AddNode) -> NumValue:
        return NumValue(self.evaluate(node.left).data + self.evaluate(node.right).data)

    def interpret_subt_node(self, node: SubtNode) -> NumValue:
        return NumValue(self.evaluate(node.left).data - self.evaluate(node.right).data)

    def interpret_mult_node(self, node: MultNode) -> NumValue:
        return NumValue(self.evaluate(node.left).data * self.evaluate(node.right).data)

    def interpret_div_node(self, node: DivNode) -> NumValue:
        lhs = self.evaluate(node.left).data
        rhs = self.evaluate(node.right).data
        # more reliable way to check if rhs == 0.0
        if math.isclose(rhs, 0.0):
            raise ValueError("Division by 0 detected")
        return NumValue(lhs / rhs)

    def interpret_plus_node(self, node: PlusNode) -> NumValue:
        return NumValue(self.evaluate(node.data).data)

    def interpret_minus_node(self, node: MinusNode) -> NumValue:
        return NumValue(-self.evaluate(node.data).data)

    def interpret_num_node(self, node: NumNode) -> NumValue:
        number = node.data
        is_float = False

        if POINT in number:
            is_float = True

        # convert number in int or float
        if is_float:
            return NumValue(float(number))
        else:
            return NumValue(int(number))


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
