# Escreva um programa que peça um número do usuário e
# calcule o logaritmo deste número nas bases 10 e 2.

# Dica: utilize o módulo math.

import math

num = float(input("Digite um valor: "))

log1 = math.log10(num)
log2 = math.log(num, 2)

print(f'O log de {num} na base 10 é {log1}')
print(f'O log de {num} na base 2 é {log2}')
