class Candidato:
    def __init__(self, rg, cpf, titulo):
        self.rg = rg
        self.cpf = cpf
        self.titulo = titulo

    def verificar (self):
        if (self.rg == True and self.cpf == True and self.titulo == True):
            return True
        else:
            return False

        