#atividade 1

h = float(input("Digite a altura do tronco: "))
Bmenor = float(input("\nDigite o valor da Base menor: "))
Bmaior = float(input("\nDigite o valor da Base maior: "))
volume =h/3*(Bmaior**2 +  Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)

print("O volume do tronco é de %.2f" % (volume))


atividade 2

horas = int(input("Digite as horas: "))

minutos = horas*60

print(" %d minuto(s)." % (minutos))


#atividade 3

idAnos = int(input("\nDigite sua idade em anos: "))
idMeses = int(input("\nDigite os meses faltantes: "))
idDias = int(input("\nDigite os dias faltantes: "))

diasTotal = (idAnos*365)+(idMeses*30)+idDias

print("Voce tem %d dia(s) de vida" % (diasTotal))


#atividade 4

valorPrestacao = float(input("\nDigite o valor da prestação: "))
multa = float(input("\nDigite a porcentagem da multa: "))
qtdeDias = int(input("\nDigite a quantidade de dias: "))

prestacao=valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)

print("O valor da sua prestação em atraso será de: R$%.2f" % (prestacao))



#atividade 5

import math
angulo = math.radians(float(input("Digite o valor, em graus, de um ângulo: \n")))

seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print("\n O seu seno é de: %f" % (seno))
print("\n O seu cosseno é de: %f" % (cosseno))
print("\n O seu tangente é de: %f" % (tangente))



