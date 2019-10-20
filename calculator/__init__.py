from calculator.controller import CalculatorController

if __name__ == '__main__':
    num1 = int(input('첫번째 수\n'))
    num2 = int(input('두번째 수\n'))
    calc = CalculatorController(num1, num2)
    op = input('연산자\n')
    result = calc.exec(op)
    print('계산결과 : %d ' % result)
    # %d 정수 %s 문장 %s 실수