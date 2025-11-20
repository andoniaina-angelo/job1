def calcule(num1: float, opérator: str, num2: float):
    if opérator == '+':
        return num1 + num2
    elif opérator== '-':
        return num1 - num2
    elif opérator == '/':
        return num1 / num2 
    elif opérator == '%':
        return num1 % num2
    else:
        return "opérator invlide"
print(calcule(6,'+',3))
