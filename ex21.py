#Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

try:
    temperatura_celsius = input("Insira a temperatura em ºC: ")
    temperatura_fahrenheit = float(temperatura_celsius) * 1.8 + 32
except ValueError as v:
    print (v)
else:
    print(f"A temperatura em graus Celsius inserida corresponde a {temperatura_fahrenheit}ºF")