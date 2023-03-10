#num = float(input("Digite um número: "))

#if num > 0 and num < 9:
#    print("Valor correto!")
#else:
#    print("Valor incorreto!")

#--- exercicio 2

#turno = str(input("Digite o seu turno (N) ou (M): "))
#qtdhoras = int(input("Digite a quantidade de horas trabalhadas: "))

#if turno == "N" or turno == "n":

#    print("Valor da hora trabalhada: R$45,00\n")
#    print("Seu salário final: R$%.2f" %(qtdhoras*45))

#elif turno == "M" or turno == "m":

#    print("Valor da hora trabalhada: R$37,50\n")
#    print("Seu salário final: R$%.2f" %(qtdhoras*37.50))



#exercício 3

#compra = float(input("Digite o valor da sua compra: "))

#if compra > 200:
#    print("Você ganhou um desconto de 20%! \n")
#    print("Sua compra foi de R$%.2f" % compra)
#   print("para R$%.2f" % (compra-(compra*0.20)))

#else:
#    print("Sua compra não passou de R$200 para conseguir o desconto.")



#exercício 4

agua = float(input("Digite o valor da conta de Água: "))
luz = float(input("Digite o valor da conta de luz: "))
telefone = float(input("Digite o valor da conta de telefone: "))
salario = float(input("Digite o valor do seu salário: "))

if (agua+luz+telefone)<salario:
    print("Seu salarío é suficiente para pagar as dívidas!")
    print("Sobrou: R$%.2f" %(salario-(agua+luz+telefone)))
else:
    print("Salário insuficiente!!")