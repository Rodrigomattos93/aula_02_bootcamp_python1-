#Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.
texto = input("Insira um texto para verificarmos se é um palíndromo: ")

if isinstance(texto, str):
    texto_corrigido = texto.replace(",", "")
    texto_corrigido = texto_corrigido.replace(".", "")
    texto_corrigido = texto_corrigido.replace("!", "")
    texto_corrigido = texto_corrigido.replace(" ", "")
    texto_corrigido = texto_corrigido.replace("-", "")
    texto_corrigido = texto_corrigido.replace("?", "")
    texto_corrigido = texto_corrigido.replace("'", "")
else:
    print("insira um valor de texto")

tamanho_texto = len(texto_corrigido)
A = 0
B = tamanho_texto-1

while A <= tamanho_texto-1:
    if texto_corrigido[A] != texto_corrigido[B]:
        break
    else:
        A=A+1
        B=B-1

if A > tamanho_texto-1:
    print("É um palíndromo")
else: 
    print("Não é um palíndromo")