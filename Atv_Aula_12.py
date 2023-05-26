import metodos_Aula_12
metodos_Aula_12.Exercicio_1
# Exercício 1 
def exercício_1():
    Km_Inicial = float(input("Digite o KM Inicial: "))
    Km_Final = float(input("Digite o KM Final:"))


    result1 = metodos_Aula_12.Exercicio_1.distancia_percorrida(Km_Inicial, Km_Final)

    result2 = metodos_Aula_12.Exercicio_1.consumo_medio(result1)

    result3 = metodos_Aula_12.Exercicio_1.valor_gasto(result1)

    print("Distância percorrida: ", result1)
    print("Consumo médio: ", result2)
    print("Valor Gasto: R$",result3)


# Exercício 2
def exercício_2():
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))

    print("A Área do retângulo é :", metodos_Aula_12.Exercicio_2.resultado_area(base, altura))

# Exercício 3
def exercício_3():

    Valor_Compra = float(input("Digite o valor da compra: "))
    Parcelas = int(input("Digite a quantidade das parcelas: "))

    print("Valor de Cada parcela:",metodos_Aula_12.Exercicio_3.valor_cada_parcela(Valor_Compra, Parcelas))

# Exercício 4
def exercício_4():
    cont = 1
    objeto = [3]
    while cont < 4:

        print(cont)
        Distancia = float(input("Digite a distancia do objeto:"))
        Tempo = float(input("Digite o tempo realizado pelo objeto:"))
        result = metodos_Aula_12.Exercicio_4.velocidade(Distancia, Tempo)
        objeto.append(result)
        cont += 1

    cont = 1
    while cont < 4:

        print("Objeto", cont)
        print("Velocidade: ", objeto[cont])

        cont += 1


# chamando cada exercício

#exercício_1()
#exercício_2()
#exercício_3()
exercício_4()