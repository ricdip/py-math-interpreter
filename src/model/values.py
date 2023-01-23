from dataclasses import dataclass


@dataclass
class NumberValue:
    value: int | float

    def __repr__(self) -> str:
        return str(self.value)
