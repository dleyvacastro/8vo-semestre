from Operation import Operation


class IntDivide(Operation):
    def __init__(self, a: float, b: float) -> None:
        super().__init__(a, b)

    def validate(self):
        if self.b == 0:
            raise ValueError("Can't divide by 0")

    def calculate(self) -> float:
        self.validate()
        return self.a // self.b
