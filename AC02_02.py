# Disciplina: ESTRUTURA DE DADOS
# Turma: BD3B NOITE
# Nome Aluno: FELIPE CHIN LAU
# Professor: JORGE CARLOS VALVERDE REBAZA
# Data entrega: 31/03/2020

'''
PERGUNTA 2: Rover Curiosity
'''
class Pilha:
    #construtor
    def __init__(self):
        self.pilha = [] 

    #metodos
    def push(self, valor):
        self.pilha.append(valor)

    def pop(self):
        return self.pilha.pop()

    def isEmpty(self):
        if len(self.pilha) == 0:
            return True
        return False

    def size(self):
        return len(self.pilha)

    def top(self):
        indice_topo = len(self.pilha) - 1
        return self.pilha[indice_topo] 

    def imprimir_c(self):
        indice = len(self.pilha) - 1
        
        while indice >= 0:
            self.pilha[indice].imprimir()
            indice = indice - 1

class Rocha:
# contrutor
    def __init__(self):
        self.rochatipo1 = []
        self.rochatipo2 = []
        self.rochatipo3 = []

# métodos 
# função para incluir Rochas.
    def incluirRocha(self, peso):                   # somente parâmetro peso, pois o diâmentro não é considerado na simulação.
        from random import randint
        tipoRocha = randint(1,3)                    # no enunciado não há definição de como separar os tipos de rochas. Assim, as rochas serão separadas randomicamente.
        if peso < 2.5:                              # condição para incluir a Rocha, e dependendo do tipo de Rocha, inclui-se na lista corresondente.
            if tipoRocha == 1:
                self.rochatipo1.append(peso)
                return('Peso da rocha {}. Rocha incluída no tipo 1'.format(peso))
            elif tipoRocha == 2:
                self.rochatipo2.append(peso)
                return('Peso da rocha {}. Rocha incluída no tipo 2'.format(peso))
            elif tipoRocha == 3:
                self.rochatipo2.append(peso)
                return('Peso da rocha {}. Rocha incluída no tipo 3'.format(peso))
            else:
                return('Peso da rocha {}. Rocha descartada.'.format(peso))
            
# função para saber o peso total das rochaas incluídas.
    def pesoTotalRochas(self):                      
        return sum(self.rochatipo1) + sum(self.rochatipo2) + sum(self.rochatipo3)

    

class Lixo:
    # contrutor
    def ___init___(self):
        self.pilhaLixo = Pilha()
    
    def incluirLixo(self, pesoLixo):
        self.pilhaLixo.push(pesoLixo)


class Curiosity:
    # constutor
    def __init__(self, pesoTotal):
        self.pesoTotal = pesoTotal





# SIMULAÇÃO
from random import randint, uniform

# lista de pedras em Marte:
lpedra = []                             # lista de pedras
npedra = randint(30,120)                # número aleatório entre 30 e 120 de elementos na lista pedra
for i in range(0,npedra):               # inserção do peso das pedras dentro de um range.
    lpedra.append(round(uniform(0.5,14.2),2))

# lista de lixos em Marte:
llixo = []                              # lista de lixos.
nlixo = randint(30,120)                 # número aleatório entre 30 e 120 de elementos na pilha lixo
for i in range(0,nlixo):                # inserção do pedo do lixo dentro de um range.
    lpedra.append(round(uniform(1.12,8.55),2))

peso = lpedra[randint(0,len(lpedra))]