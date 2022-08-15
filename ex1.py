class Animal:
    def __init__(self,especie):
        self.especie = especie

animal= Animal("cachorro")
print (animal.especie)

class Pessoa:
    def __init__ (self,altura,peso,etnia):
        self.altura = altura
        self.peso = peso
        self.etnia = etnia

    def calcular_imc (self,altura,peso):
        imc = peso / (altura * altura)

        return imc

enzo = Pessoa(1.69, 95, "italiano")
print (enzo.altura)
print (enzo.peso)
print (enzo.etnia)

imc = enzo.calcular_imc(enzo.altura,enzo.peso)
print (imc)

if imc < 18.5:
    print ("Você está abaixo do peso")
elif imc >= 18.5 and imc <= 29.9:
    print ("Você está com o peso normal")
elif imc >= 30:
    print ("Você está obeso")

