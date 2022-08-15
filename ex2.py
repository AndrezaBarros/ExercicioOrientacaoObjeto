from classes.candidato import Candidato

candidato1 = Candidato (True, True, False)
candidato2 = Candidato (False, False, False)
candidato3 = Candidato (True, True, True)

if (candidato1.verificar() == True):
    print("O Candidato1 pode ser admitido")
else:
    print("O Candidato1 não pode ser admitido")

if (candidato2.verificar() == True):
    print("O Candidato2 pode ser admitido")
else:
    print("O Candidato2 não pode ser admitido")

if (candidato3.verificar() == True):
    print("O Candidato3 pode ser admitido")
else:
    print("O Candidato3 não pode ser admitido")

