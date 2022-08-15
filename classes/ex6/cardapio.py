from classes.ex6.bebida import Bebida
from classes.ex6.comida import Comida

class Cardapio:
    def __init__(self,listaBebidas,listaComidas):
        self.listaBebidas = listaBebidas
        self.listaComidas = listaComidas

    def cadastrarBebida (self,bebida:Bebida):
        print ("*********BEBIDA*********")
        self.listaBebidas.append(bebida)
        print ("NOME: " + bebida.nomeBebida)
        print ("ML: " + str(bebida.ml))
        print ("VALOR: R$" + str(bebida.valorBebida))
        print ()

    def cadastrarComida (self,comida:Comida):
        print("*********COMIDA*********")
        self.listaComidas.append(comida)
        print ("NOME: " + comida.nomeComida)
        print ("GRAMAS: " + str(comida.gramas))
        print ("VALOR: R$ " + str(comida.valorComida))
        print ()
    
        