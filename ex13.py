#Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
texto = input("Insira um texto: ")

texto2 = texto.replace(" ", "")

print(texto2)