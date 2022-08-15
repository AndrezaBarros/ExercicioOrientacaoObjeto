from classes.colaborador import Colaborador

enzo = Colaborador("enzo", 30000, "Gerente", "09:00", "18:00")
andeza = Colaborador("andeza", 13000, "Dev. Fulstack Pl", "09:00", "17:00")
serena = Colaborador("serena", 3000, "DBA Jr", "09:00", "16:00")

irAntigoEnzo = enzo.calcularIR()
irAntigoAndeza = andeza.calcularIR()
irAntigoSerena = serena.calcularIR()

print("O valor a descontar de IR sobre o salário do " + enzo.nome + " é: " + str(irAntigoEnzo))
print("O valor a descontar de IR sobre o salário da " + andeza.nome + " é: " + str(irAntigoAndeza))
print("O valor a descontar de IR sobre o salário da " + serena.nome + " é: " + str(irAntigoSerena))

enzo.promover ("CTO", 60000)
andeza.promover("Especialista DEV", 23000)
serena.promover("DBA Pleno", 8000)

enzo.mudarHoraTrabalho("10:00", "16:00")
andeza.mudarHoraTrabalho("07:00", "15:00")
serena.mudarHoraTrabalho("08:00", "17:00")

irNovoEnzo = enzo.calcularIR()
irNovoAndeza = andeza.calcularIR()
irNovoSerena = serena.calcularIR()

print("O valor a descontar de IR sobre o salário do " + enzo.nome + " é: " + str(irNovoEnzo))
print("O valor a descontar de IR sobre o salário da " + andeza.nome + " é: " + str(irNovoAndeza))
print("O valor a descontar de IR sobre o salário da " + serena.nome + " é: " + str(irNovoSerena))

