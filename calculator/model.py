class CalculatorModel: #class이름 대문자
    #시작하는 method
    def __init__(self, num1, num2): #entry point 여기서 숫자를 받는다
        self.num1 = num1
        self.num2 = num2

    def add(self):
        result = self.num1 + self.num2
        return result

    def sub(self):
        result = self.num1 - self.num2
        return result

    def mul(self):
        result = self.num1 * self.num2
        return result

    def div(self):
        result = self.num1 / self.num2
        return result
