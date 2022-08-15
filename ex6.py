# Classe: Lanchonete / Atributos: Cadardápio, Conta, bebidas e comidas pedidas (listar pedidos)
# Métodos: Calcular Conta
# Classe: Cardápio / Atributos: lista de bebidas e comidas
# Método: Cadastrar Bebida (input interno) / parâmetro: classe bebida
# Método: Cadastrar Comida (input interno) / parâmetro: classe comida
# Método: pedir Bebida (input externo) - Deve adicionar valor a conta no final
# Método: pedir Comida (input externo) - Deve adicionar valor a conta no final
# Classe: Comida / Atributos: Nome do prato e a quantidade de gramas e valor
# Classe: Bebida / Atributos: Nome da bebida e quantos Ml ela tem e valor

from classes.ex6.lanchonete import Lanchonete
from classes.ex6.cardapio import Cardapio
from classes.ex6.bebida import Bebida
from classes.ex6.comida import Comida

#ITENS DO CARDÁPIO - COMIDAS#

comida1 = Comida("Strogonoff", 150, 30.00)
comida2 = Comida("Mac and Cheese", 200, 42.50)
comida3 = Comida("Cesar Salad", 100, 40.00)
comida4 = Comida("Baião de Dois", 200, 50.00)
comida5 = Comida("Escondinho de Carne Seca", 200, 55.00)

#ITENS DO CARDÁPIO - BEBIDAS#

bebida1 = Bebida("Suco de Laranja", 350, 10.00)
bebida2 = Bebida("Coca Cola", 300, 7.00)
bebida3 = Bebida("Água com Gás", 250, 3.50)
bebida4 = Bebida("Milkshake", 350, 13.00)
bebida5 = Bebida("H2O", 260, 7.00)

cardapio = Cardapio ([],[])

cardapio.cadastrarComida(comida1)
cardapio.cadastrarComida(comida2)
cardapio.cadastrarComida(comida3)
cardapio.cadastrarComida(comida4)
cardapio.cadastrarComida(comida5)

cardapio.cadastrarBebida(bebida1)
cardapio.cadastrarBebida(bebida2)
cardapio.cadastrarBebida(bebida3)
cardapio.cadastrarBebida(bebida4)
cardapio.cadastrarBebida(bebida5)

lanchonete = Lanchonete([])

lanchonete.bebidasPedidas(3)
lanchonete.bebidasPedidas(2)

lanchonete.pedirBebidas.calcularConta()
