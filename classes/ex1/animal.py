class Animal:
    def __init__(self, npatas, especie):
        self.npatas = npatas
        self.especie = especie

    def locomover (self, metodolocomocao):
        print("Este animal " + metodolocomocao)
        if (self.npatas == 2):
            print("Este animal é um bípede")
        elif (self.npatas == 4):
            print("Este animal é um quadrúpede")
        else:
            print("Não foi possível identificar este animal")
    
    