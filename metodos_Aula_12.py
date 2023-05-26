class Exercicio_1:

    def distancia_percorrida(Km_Inicial, Km_Final):

        result = 0
        cont = 0

        if Km_Inicial < Km_Final:

            cont = Km_Final - Km_Inicial

        else:

            cont = 0

        return cont
    
    def consumo_medio(Km_rodados):

        Km_Gasolina = 0.43

        result = Km_Gasolina * Km_rodados

        return result
    
    def valor_gasto(Km_rodados):

        Gasto_por_Km = 0.54

        result = Gasto_por_Km * Km_rodados

        return result
    
class Exercicio_2:

    def resultado_area(base, altura):

        area = base * altura

        return area

class Exercicio_3:

    def valor_cada_parcela(compra, parcelas):

        if parcelas > 0:

            result1 = (compra / parcelas) * 1.05

            return result1

        else:
            return compra
        
class Exercicio_4:

    def velocidade(distancia, tempo):

        velocidade = distancia / tempo

        return velocidade


