# Faça um programa que peça 5 números de ponto flutuante do usuário
# e apresente no final a média dos números digitados.

print("Digite 5 numeros para calcular a média dele\n")

num1 = float(input("Digite numero 1 : "))
num2 = float(input("Digite numero 2 : "))
num3 = float(input("Digite numero 3 : "))
num4 = float(input("Digite numero 4 : "))
num5 = float(input("Digite numero 5 : "))

media = (num1 + num2 + num3 + num4 + num5)/5

print(f"A média entre eles é de ", {media})
