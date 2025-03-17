#Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

try:
    num1 = float(input("Entrada numérica 1: "))
    num2 = float(input("Entrada numérica 2: "))
    operador = input("Insira um operador (+, -, *, /): ")

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        resultado = num1 / num2 

    print(resultado)       
except ValueError:
    print("Valor inserido errado")

except ZeroDivisionError:
    print("Não consigo fazer uma divisão por zero")

except NameError:
    print("O operador inserido não é comportado pelo programa")