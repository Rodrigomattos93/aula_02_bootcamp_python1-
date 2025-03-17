#Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

try:
    lista = input("Insira uma lista de números inteiros separados por vírgula: ")
    lista2 = lista.split(",")
    A = 0
    while A <= len(lista2)-1:
        lista2[A] = int(lista2[A])
        A = A+1
    
    print(lista2)

except:
    print("Mensagem de erro: lista inserida não é composta por números inteiros.")