

def hello_world() -> str:
    return "Hello World"


class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def add(val1, val2):
        return val1 + val2

    @staticmethod
    def susbtr(val1, val2):
        return Calculator.add(val1, -val2)
