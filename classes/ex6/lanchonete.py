from classes.ex6.cardapio import Cardapio

class Lanchonete:
    def __init__(self,cardapio):
        self.cardapio = cardapio
        self.conta = 0
        self.bebidasPedidas = []
        self.comidasPedidas = []

    def pedirBebidas(self,bebida):
        self.bebidasPedidas.append (bebida)
        print ("Por favor escolha suas bebidas, considerando o código do cardápio: \n")
       
    def pedirComidas(self,comida):
        self.comidasPedidos.append (comida)
        print ("Por favor escolha suas comidas, considerando o código do cardápio: \n")
    
    def calcularConta (itensPedidos):
        valorBebidas = 0

        for bebida in self.bebidasPedidas:
            valorBebidas = valorBebidas + bebida.valorBebida
        
        print("Valor das bebidas: " + str(valorBebidas))




    


    