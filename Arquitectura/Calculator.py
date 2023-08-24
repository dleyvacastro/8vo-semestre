from ALU import ALU


class Calculator:
    def __init__(self) -> None:
        self.alu: ALU = ALU()
        self.operator: bool = False

    def menu(self) -> None:
        while 1:
            if self.operator:
                self.operator = False
                self.alu.process_operator()
            else:
                self.operator = True
                self.alu.process_operand()

    def main(self) -> None:
        self.menu()


if __name__ == '__main__':
    calc = Calculator()
    calc.main()
