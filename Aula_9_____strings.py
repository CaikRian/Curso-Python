# Aula 9_____strings


str1 = "Hello_Python" #uma sequencia de caracteres
str2 = 'Hello_Python' #cada letra irá virar um ídice (a partir do 0)

letra = str2[0] #quero o caractere do índice 0
print(letra)

qtd = len(str2) #retorna a quantidade de caratere da string
print(qtd) 



# Conta a quantidade de caractere de um texto
num = input("Digite um número inteiro: ")
t = len(str(num))
print("quantidade de caractere(s):", qt)


# inverte o texto digitado
string = input("Digite um texto: ")
inversa = " "
for x in string:
    inversa = x + inversa
print(inversa)


s = "ABC"
print(s + "D")

idade = 17
nome = "Caik"
print("%03d" %idade) # formata a exibição utilizando a composição
print("%.2f" %idade) # coloca duas casas depois da virgula

print(f"Meu nome é {nome} e eu tenh {idade} de idade") #Forma utilizando FString
print("Meu nome é {} e eu tenho {} de idade".format(nome, idade)) # Utilizando Format

#_____ Fatiamento

fruit = "banana"
print(fruit[:3]) # fatia do INICIO até a posição 3
print(fruit[3:]) # fatia do FINAL até a posição 3
print(fruit[0:-2]) # fatia do final para o inicio, excluindo as duas ultimas posições

# _____ Programa que exibe o numero inteiro em inverso
num = input("Digite um numero inteiro:")
num = num[::-1]
print(num)


#____STRIP()____Tira todos os espaços em branco do inicio e no final de uma variavel
b = "   Fizeram as atividades?   "
result = b.strip()
print(result)

#___IN____ verifica se uma substring e parte de uma outra string

a = "Fiz nao"
rst1 = "nao" in a
rst2 = "sim" in a 
print( rst1 , rst2)

#__FIND___ retorna onde a substring começa na string

a = "Fiz nao"
rst1 = a.find("sim") #Vai retornar -1 se o result for false
rst2 = a.find("nao")
print( rst1 , rst2)


#_REPLACE__ serve para trocar todas as odocrrencias de uma substring por outra

a = "Fizeram a atividade?"
rst1 = a.replace("atividade", "avaliação") #O VALOR DE 'a' NÃO FOI ALTERADO PELO REPLACE
print( rst1 )

#__SPLIT(SEP)__ separa uma string usando sep como separador. Retorna uma lista de substrings

num = "1; 2; 3"
rst1 = num.split(";")
print(rst1)

num = "Caik Rian Gadelha"
rst1 = num.split()
print(rst1)

#__lower__ deixa o caracter em caixa baixa
a = "AtIvIdAdE"
a1 = a.lower()
print(a1)

#__upper__ deixa o caracter em caixa alta
a = "AtIvIdAdE"
a2 = a.upper()
print(a2)
#__count__ retorna quantas vezes o elemento aparece na string

frase = "O rato roeu a roupa do rei de roma"
rst1=frase.count("r")
print(rst1)


#________programa que conta o numero de palavras de um texto

texto = input("Digite um texto: ")
pontuacao = [".", ",", ":", ";", "!", "?"]

#remove os sinais de pontuação
for p in pontuacao:
    texto = texto.replace(p," ")

# split devolve lista com palavras como itens

numero_palavras = len(texto.split())
print("Numero de palavras:", numero_palavras)

#______Programa que calcula o lucro de uma empresa a partir da anetrada do faturamento e do custo de produção

#resolução utilizando replace

faturamento = float(input("Digite o faturamento: R$ "))
custo = float(input("Digite o custo: R$"))
lucro = faturamento - custo
lucro = f"R$ {lucro:_.2f}"
lucro = lucro.replace(".", ",").replace("_", ".")
print(f"O lucro foi de R${lucro}")
