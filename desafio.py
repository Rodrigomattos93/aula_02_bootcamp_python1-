try:
    nome = ""
    while len(nome) == 0:
        nome = input("Insira seu nome: ")

    salario = float(input("Insira seu salário: "))
    bonus = float(input("Insira seu percentual de bonus: "))
    resultado = 1000 + bonus * salario
    print(f"Olá, {nome}. Seu valor de bônus é {resultado}")

except ValueError as e:
    print(e)