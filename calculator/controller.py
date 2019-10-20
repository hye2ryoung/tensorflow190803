from calculator.model import CalculatorModel #모듈 호출 import 클래스

class CalculatorController:
    def __init__(self,num1,num2):
        self.calc = CalculatorModel(num1,num2) #CalculatorModel클래스에대한 인스턴스 (calc), 생성자 (CalculatorModel)

    def exec(self, op):
        if op == '+':
            result = self.calc.add()

        elif op == '-':
            result = self.calc.sub()

        elif op == '*':
            result = self.calc.mul()

        elif op == '/':
            result = self.calc.div()

        return result