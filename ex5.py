# Classe: PetShop
# terá os atributos: lista de pets, lista de atendentes
# Método: Cadastrar pet / parametro: pet
# Metodo: cadastrar atendente / parametro: atendente


# Classe: Pet
#atributos: nome, espécie e porte do pet
#método: verificar humor do pet / return: Feliz ou triste

# Classe: Atendente
#Atributos: Nome, idade, energia (cansado ou disposto - começa com 100% de energia, e a cada atendimento tira a porcentaagem de acordo com o porte do  de energia)
#Método: atender Pet / Parametro: o pet que ele vai atender

from classes.pet import Pet
from classes.atendente import Atendente
from classes.petshop import PetShop

pet1 = Pet("Suzi","Porquinho da India", "Pequeno", "Feliz")
pet2 = Pet("Lucca", "Border Collie", "Médio", "Triste")
pet3 = Pet("Mel", "Cavalo", "Grande", "Feliz")
pet4 = Pet("Bethoven", "BullDog", "Médio", "Triste")
pet5 = Pet("Zoe", "Capivara", "Médio", "Feliz")

atendente1 = Atendente("Aline", "24 anos", 100)
atendente2 = Atendente("Marcia", "30 anos", 100)
atendente3 = Atendente("Xolis", "25 anos", 100)

petshop = PetShop([], [])

petshop.cadastrarPet(pet1)
petshop.cadastrarPet(pet2)
petshop.cadastrarPet(pet3)
petshop.cadastrarPet(pet4)
petshop.cadastrarPet(pet5)

petshop.cadastrarAtendente(atendente1)
petshop.cadastrarAtendente(atendente2)
petshop.cadastrarAtendente(atendente3)

petshop.listaAtendente[0].atenderPet(pet1)
petshop.listaAtendente[1].atenderPet(pet2)
petshop.listaAtendente[1].atenderPet(pet3)
petshop.listaAtendente[1].atenderPet(pet4)
petshop.listaAtendente[2].atenderPet(pet5)

petshop.listaAtendente[0].verificarEnergiaAtendente()
petshop.listaAtendente[1].verificarEnergiaAtendente()
petshop.listaAtendente[2].verificarEnergiaAtendente()


