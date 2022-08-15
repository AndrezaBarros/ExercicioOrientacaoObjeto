from classes.pet import Pet

class Atendente:
    def __init__(self, nomeAtendente, idade, energia):
        self.nomeAtendente = nomeAtendente
        self.idade = idade
        self.energia = energia
        self.energiaAtual = self.energia

    def atenderPet (self,pet):
        if (self.energiaAtual <= 20):
            print("O(a) atendente " + self.nomeAtendente + " está muito cansado(a) para atender o(a) cliente " + pet.nomePet + " - Favor selecionar outro atendente!")
            print ()
        else:
            print ("O(a) atentende " + self.nomeAtendente + " irá atender o Pet: ")
            print ("NOME: " + pet.nomePet)
            print ("ESPECIE: " + pet.especie)
            print ("PORTE: " + pet.porte)
            print ("HUMOR: " + pet.humor)
            print ()
            if (pet.porte == "Pequeno"):
                self.energiaAtual = self.energiaAtual - 20
            elif (pet.porte == "Médio"):
                self.energiaAtual = self.energiaAtual - 30
            elif (pet.porte == "Grande"):
                self.energiaAtual = self.energiaAtual - 50

    def verificarEnergiaAtendente (self):
        print ("** " + self.nomeAtendente + "**")
        print("Situação de energia: " + str(self.energiaAtual) + "%")
        print ()
        
        
    