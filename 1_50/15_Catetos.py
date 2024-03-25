# Elabore um programa para calcular a hipotenusa de um triângulo.

# Dicas: Veja o módulo math (math.hypot)

# Utilize a seguinte fórmula: hipotenusa=(a²+b²)¹/2:

cO = float(input(f"Digite o valor do cateto oposto: "))
cA = float(input(f"Digite o valor do cateto adjacente: "))

hipotenusa = (cO*cO)+(cA*cA)/2

print(f"Hipotenusa = {hipotenusa}")
