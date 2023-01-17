from dataclasses import dataclass


@dataclass
class NumValue:
    data: int | float

    def __repr__(self) -> str:
        return str(self.data)
