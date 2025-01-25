import random

noveDigitos = ""

for i in range(9):
    noveDigitos += str(random.randint(0,9)) #gera um número aleatório de 0 a 9

contadorRegressivo1 = 10

resultadoDigito1 = 0
for digito in noveDigitos:
    resultadoDigito1 += int(digito) * contadorRegressivo1
    contadorRegressivo1 -= 1

digito1 = (resultadoDigito1 * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0

dezDigitos = noveDigitos + str(digito1)
contadorRegressivo2 = 11

resultadoDigito2 = 0
for digito in dezDigitos:
    resultadoDigito2 += int(digito) * contadorRegressivo2
    contadorRegressivo2 -=  1

digito2 = (resultadoDigito2 * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0

cpfGerado = f"{noveDigitos}{digito1}{digito2}"
print(cpfGerado)

print("CPF gerado!")