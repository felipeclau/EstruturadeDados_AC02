class Lixo:
    # contrutor
    def ___init___(self):
        self.pilhaLixoMetal = []               # Lista para lixo do tipo metal.
        self.pilhaLixoFunk = []                # Lista para lixo do tipo não metal.

# função para incluir lixo metal
    def incluirLixoMetal(self, pesoLixo):
        self.pilhaLixoMetal.append(pesoLixo)

x = Lixo()
x.incluirLixoMetal(2)
