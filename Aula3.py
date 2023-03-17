#exemplo 1

num = int(input("Digite um número com três digitos: "))
d1 = num // 100
d2 = num % 100 // 10
d3 = num % 10
inverso = d3*100+d2*10+d1
print("O inverso do número digitado é: ", inverso)



#exemplo 2

import math
num = float(input("Digite um número: "))
resultado = math.sqrt(num)
print("O valor da raiz quadrada é: ", resultado)


#exemplo 3

import math
num = float(input("Digite um número real: "))
absoluto = math.fabs(num)
inteiro = math.trunc(num)
raiz = math.sqrt(absoluto)
fatorial = math.factorial(math.fabs(inteiro))

print("Absoluto: ", absoluto)
print("Inteiro: ", inteiro)
print("Raiz: ", raiz)
print("Fatorial: ", fatorial)


#exemplo 4

import math
raio = float(input("Digite o raio da circuferência em cm: "))
comprimento = 2 * math.pi * raio
area = math.pi * raio * raio
print("O comprimento da circuferência é igual a %.2f cm\n" % (comprimento))
print("A área da circuferência é igual a %.2f cm²" %(area))



#exemplo 5

import math
sombra = float(input("Digite o comprimento da sombra em m: "))
angulo = math.radians(float(input("Digite o ângulo em graus: ")))
altura = math.tan(angulo) * sombra
print("A altura do prédio é de %.2f m" % (altura))




















