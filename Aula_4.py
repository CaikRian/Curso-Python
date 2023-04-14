#Atividade 1
result = 0

for i in range(101):
   result = i % 2
  
 if result == 0:
    print(i)


#Atividade 2

for i in range(100):
    i=i+1
    if i >=1 and i<=50:
        print(i)
    elif i >= 52 and i<=100:
        result = i % 2
        
        if result == 0:
            print(i)


#Atividade 3

num = 0
while num < 1:
    num = int(input("Digite um valor (inteiro e positivo): "))
    for i in range(num):
        i = i+1
        soma =+ 1/i
    print("Valor da soma i/num: ", soma)



 #Atividade 4

resp = "s"
contP = 0
contN = 0
NumMin = 0

while resp == "s" or resp == "S":

    num = float(input("Digite um valor: "))
    if NumMin > num:
        NumMin = num
    
    if num > 0:
        contP = contP + 1
    else:
        contN = contN + 1

    resp = str(input("Deseja digitar mais um? (S/N): "))

print("Você Digitou",contP,"número(s) Positivo(s)\n")
print("Você Digitou",contN,"número(s) Negativo(s)")
print("O menor número digitado é: ",NumMin)


#Atividade 5

resp1 = "s"
Npessoa = 0
ContF = 0
ContM = 0
sexo = "s"
altura = 0
SomaAlturaF = 0
SomaAlturaM = 0
MediaAlturaF = 0
MediaAlturaM = 0

while Npessoa < 1:

    Npessoa = int(input("Digite a quantidade de pessoasa  serem registradas: "))

    for i in range(Npessoa):
        cont =+ 1
        print(cont,"ª Pessoa\n")

        while sexo != "F" or sexo != "f" or sexo != "M" or sexo != "m":

            sexo = str(input("Digite o Sexo: (F/M)"))


        if sexo == "F" or sexo == "f":
           
            while altura < 1 :

                altura = float(input("Digite a altura(acima de 1m):"))
            
            SomaAltura =+ altura
            ContF = ContF + 1
            MediaAlturaF = SomaAlturaF/ContF

        else:
    
                while altura < 1 :

                    altura = float(input("Digite a altura(acima de 1m):"))
            
SomaAltura =+ altura
ContM = ContM + 1
MediaAlturaM = SomaAlturaM/ContM

print("Quantidade de mulheres: ",ContF)
print("\nA media da altura entre as mulheres é de: ", MediaAlturaF)
print("\nQuantidade de mulheres: ",ContM)
print("A media da altura entre as mulheres é de: ", MediaAlturaM)
           








    







        
    

        
    


    
    


  

