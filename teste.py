class Lixo:
    # contrutor
    def ___init___(self):
        self.pilhaLixoMetal = []              # Lista para lixo do tipo metal.
        self.pilhaLixoFunk = []                # Lista para lixo do tipo não metal.

# função para incluir lixo metal
    def incluirLixoMetal(self, valor):
        self.pilhaLixoFunk.append(valor)

class Figuras:
    #construtor
    def __init__(self):
        self.lista_quadrados = []

    #metodos
    def setQuadrado(self, quadrado):
        self.lista_quadrados.append(quadrado)

x = Lixo()
#x.incluirLixoMetal(2)

y = Figuras()
y.lista_quadrados(2)