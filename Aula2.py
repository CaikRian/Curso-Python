#\ -------exemplo 01

 idade = int(input("Digite sua idade: \n"))

 if idade >=18:
    print("Você PODE ter sua CNH!!")


#\ -------exemplo 02

 num = int(input("Digite um número inteiro: \n"))
 if num % 2 == 0:
   print("O número: ", num, " é par")


#\ -----exemplo 03

 n1 = int(input("Digite o valor A: \n"))
 n2 = int(input("Digite o valor B: \n"))
 n3 = int(input("Digite o valor C: \n"))

 if n1 > n2 and n3 > n2:
 print("O menor valor é o B")


#\ -------exemplo 04

 idade = int(input("Digite sua idade: \n"))
 if idade >=18:
     print("Você PODE ter sua CNH!!")
 else: 
     print("Você NÃO pode ter sua CNH")


#\ -------exemplo 05

 num = int(input("Digite um número inteiro: \n"))
 if num % 2 == 0:
  print("O número: ", num, " é par")
 else:
  print("O número: ", num, " é ímpar")


#\ -------exemplo 06

 n1 = float(input("Digite a 1ª nota: "))
 n2 = float(input("Digite a 2ª nota: "))

 media= (n1+n2)/2

 if media >= 6:
     print("Aprovado!")
 else:
     print("Reprovado!!")

#\ -------exemplo 06

import math
n1 = int(input("Digite um número: "))
if n1 > 0:
    r = math.sqrt(n1)
    print("A raiz quadrada  de %.2f é %.2f" % (n1, r))
else:
    print("Não existe raíz quadrada de número negativo")

