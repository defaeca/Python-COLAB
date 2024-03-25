# Escreva um programa que peça dois números e apresente a divisão e multiplicação entre eles.
# A tela de apresentação deverá seguir o seguinte formato:

# "[número1]x[número2]=[multiplicação]"

# "[número1]/[número2]=[divisão]"

n1 = float(input("Digite valor n1:"))
n2 = float(input("Digite valor n2:"))

multi = float(n1 * n2)
divi = float(n1 / n2)

print((f"{multi} é a multiplicação entre eles"))
print((f"{divi} é a divisao entre eles"))
