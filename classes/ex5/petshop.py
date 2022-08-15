from classes.atendente import Atendente
from classes.pet import Pet

class PetShop:
    def __init__(self, listaPets, listaAtendente):
        self.listaPets = listaPets
        self.listaAtendente = listaAtendente

    def cadastrarPet (self,pet:Pet):
        self.listaPets.append(pet)
        print("**CLIENTE**")
        print ("NOME:  " + pet.nomePet)
        print ("ESPECIE: " + pet.especie)
        print ("PORTE: " + pet.porte)
        print("HUMOR: " + pet.humor)
        print ()

    def cadastrarAtendente (self,atendente:Atendente):
        self.listaAtendente.append(atendente)
        print("**ATENDENTE**")
        print ("NOME: " + atendente.nomeAtendente)
        print ("IDADE: " + atendente.idade)
        print ("ENERGIA: " + str(atendente.energia) + "%")
        print ()

    


  
