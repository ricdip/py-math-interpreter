from .lexer import Lexer
from .parser import Parser
from .interpreter import Interpreter


def main():
    text = "1+2*3-(1.5*-2)*(1+1)"
    # lexical analysis: text: str -> tokens: List[Token]
    lexer = Lexer(text)
    tokens = lexer.scan()
    # syntax analysis: tokens: List[Token] -> ast: AST (Abstract Syntax Tree)
    parser = Parser(tokens)
    ast = parser.parse()
    # interpretation: ast: AST -> output: NumOutput (wrapper for calculation result: int | float)
    interpreter = Interpreter(ast)
    output = interpreter.interpret()

    print()
    print(f"input: {text}", end="\n\n")
    print(f"tokens: {tokens}", end="\n\n")
    print(f"ast: {ast}", end="\n\n")
    print(f"output: {output}", end="\n\n")


if __name__ == "__main__":
    main()
