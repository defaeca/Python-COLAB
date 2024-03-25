# Faça um programa que peça uma temperatura em Fahrenheit (F) e converta esta temperatura para
# grau Celsius (C), mostrando o resultado da conversão na tela.

# Use a fórmula: C = 5 * ((F-32) / 9).
from math import *
f = float(input("Digite um valor de uma temperatura em Fahrenheit: "))
c = 5 * ((f - 32) / 9)

print(f"O valor de {f:.2}° convertendo em Celsius é {c:.2}°")
