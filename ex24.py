#Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

try:
    num = float(input("Insira um valor numérico: "))

    if num > 0:
        a = "positivo"
    elif num < 0:
        a = "negativo"
    elif num == 0:
        a = "zero"
    
    if num % 2 == 0:
        b = "par"
    elif num % 2 == 1:
        b = "ímpar"
        
    print(f"O número é {a} e {b}")
except ValueError:
    print("Valor não numérico inserido")