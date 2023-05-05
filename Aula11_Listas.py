# ------ LISTAS
# 1º exemplo
nomes = []
for i in range (5):
    n = input("Digite um nome: ")
    nomes.append(n)

for x in range (5):
    print(nomes[x])

# ----------------------------------------------
 # criação de lista em python

"""
nome = []
nome = list()
teste = ["mamão", 10, 1.5]

--------------------> TODAS ESSAS CRIAM ARRAY

remove(x) = TIRA O PRIMEIRO ITEM DA LISTA COM ESSE VALOR
teste.remove("mamão") 
enumerate(x) ---> gera uma tupla em que o primeiro valor é o índice 
                     e o segundo é o elemento da lista sendo enumerada 
***** tuplas são imutáveis
"""

# ---> Atividade 1

notas = [6, 7, 6.5, 4.8, 8]
soma = 0
for i in range(5):
    soma += notas[i]

media = soma/5
print("Média: %.2f" %media)


# ---> Atividade 2
nomes = []
for i in range(5):
    n - input("Digite um nome: ")
    nomes.append(n)
print(nomes)
n = int(input("Digite um número: "))
print(nomes[n])


# ---> Atividade 3
num = []
soma = 0

while True:
    n = int(input("Digite um número inteiro: "))
    if n == 0:
        break
    num.append(n)
    soma += n

media = soma/len(num)
print("%.2f"%media)
print(num)


# ---> Atividade 4
notas = []
soma = 0
n = int(input("Entre com o número de notas: "))
for i in range(1, n + 1):
    nota = float(input("Entre com a %dª nota: "%i))
    notas.append(nota)
    soma += nota
print(notas)

media = soma/n
print("%.2f"%media)



# ----------> Atividade 5
lugaresvagos = [10,2,3,4,0]
x=1
print("Bem vindos ao CINEMARKO")
for s in lugaresvagos:
    print("Sala %d: %d lugares vagos"%(x,s))
    x+=1
while True:
    sala = int(input("Escolha uma sala (0 para sair): "))
    if sala == 0:
        print("Até logo")
        break
    elif sala>len(lugaresvagos):
        print("Sala inválida!!\n")
    elif lugaresvagos[sala-1]==0:
        print("Desculpe! Sala Lotada!\n")
    else:
        compra = int(input("Quantos ingressos você deseja (%d vagos) :"%lugaresvagos[sala-1]))
        if compra>lugaresvagos[sala-1]:
            print("Desculpe! Número de ingressos indisponíveis\n!!")
        elif compra<=0:
            print("Número inválido\n")
        else:
            lugaresvagos[sala-1]-=compra
            print("%d ingressos vendidos! Bom filme"%compra)
            break
print("Utilização das salas:")
for x, s, in enumerate(lugaresvagos):
    print("Sala %d - %d lugar(es) vago(s)"&(x-1,s))



# ----------> Atividade 6
medias = []
nomes = []

x = int(input("Digite a quantidade de alunos: "))
for i in range(x):
    nome = input("Digite o nome dos aluno: ")
    n1 = float(input("Digite a 1ª nota: "))
    n2 = float(input("Digite a 2ª nota: "))
    media = (n1+n2) / 2
    medias.append(media)
    nomes.append(nome)

n = int(input("Digite o nº do aluno que deseja exibir: "))
if medias[n] >= 6.0:
    print("O aluno %s foi APROVADO com média %.2f"%(nomes[n],medias[n]))
else:
    print("O aluno %s foi REPROVADO com média %.2f"%(nomes[n],medias[n]))




# ----------> Atividade 7

# -> Crição da lista
nomes = []
#armazenar os valores na lista
for i in range(5):
    n = input("Digite um nome: ")
    nomes.append(n) #adiciona no final da lista
    #nomes.insert(i, n)

print(nomes) #mostra os itens da lista
print(len(nomes)) #quantidade de itens da lista
#exclui um item da lista
nome = input("Digite um nome para remover da lista: ")
if nome in nomes:
    nomes.remove(nome) #remove o nome da lista
    print(nomes)
    print(len(nomes))
else:
    print("Nome não encontrado")
