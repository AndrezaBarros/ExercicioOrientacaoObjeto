class Colaborador:
    def __init__(self,nome,salario,cargo,horaEntrada,horaSaida):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        self.horaEntrada = horaEntrada
        self.horaSaida = horaSaida

    def promover (self,novoCargo,novoSalario):
        print(self.nome + " :\n cargo antigo = " + self.cargo + " novo cargo = " + novoCargo + "\n salario antigo = " + str(self.salario) + " salario novo = " + str(novoSalario))
        self.cargo = novoCargo
        self.salario = novoSalario

    def mudarHoraTrabalho (self,novaHoraEntrada,novaHoraSaida):
        print(self.nome + ":\n horário de entrada antigo = " + self.horaEntrada + " horario de entrada novo = " + novaHoraEntrada + "\n horario de saida antigo = " + self.horaSaida + " horario de saida novo = " + novaHoraSaida)
        self.horaEntrada = novaHoraEntrada
        self.horaSaida = novaHoraSaida

    def calcularIR (self):
        if (self.salario <= 1903.98):
            return 0
        elif (self.salario >= 1903.99 and self.salario <= 2826.65):
            return (self.salario * 0.075) - 142.80
        elif (self.salario >= 2826.66 and self.salario <= 3751.05):
            return (self.salario * 0.15) - 354.80
        elif (self.salario >= 3751.06 and self.salario <= 4664.68):
            return (self.salario * 0.225) - 636.13
        elif (self.salario >= 4664.68):
            return (self.salario * 0.275) - 869.36
    
        