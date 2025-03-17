#Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
texto = input("Insira um texto: ")

lista = texto.split("/")
dia = lista[0]
mes = lista[1]
ano = lista[2]

print(f"o dia da data inserida eh {dia}. O mes da data inserida eh {mes}. O ano da data inserida eh {ano}")