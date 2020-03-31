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
# incluir valor.    
    def push(self, valor):                              
        self.pilha.append(valor)
# retirar valor.
    def pop(self):
        return self.pilha.pop()
# identificar se a pilha está vazia.
    def isEmpty(self):
        if len(self.pilha) == 0:
            return True
        return False
# tamanho da pilha.
    def size(self):
        return len(self.pilha)
# índice o "topo" da pilha.
    def top(self):
        indice_topo = len(self.pilha) - 1
        return self.pilha[indice_topo] 
# impressão 
    def imprimir_c(self):
        indice = len(self.pilha) - 1
        
        while indice >= 0:
            self.pilha[indice].imprimir()
            indice = indice - 1

class Rocha:
# contrutor
    def __init__(self):
        self.rochatipo1 = []                        # Lista para rochas do tipo 1.
        self.rochatipo2 = []                        # Lista para rochas do tipo 2.
        self.rochatipo3 = []                        # Lista para rochas do tipo 3.

# métodos 
# função para incluir Rochas.
    def incluirRocha(self, peso):                   # somente parâmetro peso, pois o diâmentro não é considerado na simulação.
        from random import randint
        tipoRocha = randint(1,3)                    # no enunciado não há definição de como separar os tipos de rochas. Assim, as rochas serão separadas randomicamente.
        if peso < 2.5:                              # condição para incluir a Rocha, e dependendo do tipo de Rocha, inclui-se na lista corresondente.
            if tipoRocha == 1:
                self.rochatipo1.append(peso)
                print('Peso da rocha {}. Rocha incluída no TIPO 1'.format(peso))
            elif tipoRocha == 2:
                self.rochatipo2.append(peso)
                print('Peso da rocha {}. Rocha incluída no TIPO 2'.format(peso))
            else:
                self.rochatipo2.append(peso)
                print('Peso da rocha {}. Rocha incluída no TIPO 3'.format(peso))
        else:
            print('Peso da rocha {}. Rocha descartada.'.format(peso))
            
# função para saber o peso total das rochaas incluídas.
    def pesoTotalRochas(self):                      
        return float(sum(self.rochatipo1) + sum(self.rochatipo2) + sum(self.rochatipo3))

# função para equilibrar a lista
    def retirarPedras(self):
        diferenca = 2                                   # variável para calcular a diferença entre o tamanho das listas.
        while diferenca > 1:            
            q1 = len(self.rochatipo1)                   # variável para tamanho da lista do tipo de rocha
            q2 = len(self.rochatipo2)                   # variável para tamanho da lista do tipo de rocha
            q3 = len(self.rochatipo3)                   # variável para tamanho da lista do tipo de rocha
            
            maiorQ = 0                                  # verificar qual das listas possui maior número de elementos
            if q1 > q2 and q1 > q3:
                maiorQ = q1
            elif q2 > q1 and q2 > q3:
                maiorQ = q2
            else:
                maiorQ = q3
            
            menorQ = 0                                  # verificar qual das listas possui menor número de elementos
            if q1 < q2 and q1 < q3:
                menorQ = q1
            elif q2 < q1 and q2 < q3:
                menorQ = q2
            else:
                menorQ = q3
            
            diferenca = maiorQ - menorQ                 # calcular a diferença do maior número para o menor
            if diferenca > 1:                           # a diferença do maior para o menor vai servir para abater elementos da maior lista
                    if maiorQ == q1:
                        while menorQ < len(self.rochatipo1)-1:
                            self.rochatipo1.pop(len(self.rochatipo1)-1)
                    if maiorQ == q2:
                        while menorQ < len(self.rochatipo2)-1:
                            self.rochatipo2.pop(len(self.rochatipo2)-1)
                    if maiorQ == q3:
                        while menorQ < len(self.rochatipo3)-1:
                            self.rochatipo3.pop(len(self.rochatipo3)-1)
        print('Rochas retiradas. Tipos de rochas equilibradas.')
        

class Lixo:
# contrutor
    def ___init___(self):
        self.pilhaLixoMetal = Pilha()               # Lista para lixo do tipo metal.
        self.pilhaLixoFunk = Pilha()                # Lista para lixo do tipo não metal.

# função para incluir lixo metal
    def incluirLixoMetal(self, pesoLixo):
        return self.pilhaLixoMetal.push(pesoLixo)

# função para incluir lixo não metal
    def incluirLixoFunk(self, pesoLixo):
        return self.pilhaLixoFunk.push(pesoLixo)

# função para saber o peso total
    def pesoTotalLixo(self):
        return float(sum(self.pilhaLixoMetal) + sum(self.pilhaLixoFunk))

class Curiosity:
# constutor
    def __init__(self, pesoTotalRocha, pesoTotalLixo):
        self.pesoTotalRocha = pesoTotalRocha
        self.pesoTotalLixo = pesoTotalLixo
# método
    def pesoCuriosity(self):
        return float((self.pesoTotalRocha + self.pesoTotalLixo))
    
        





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
    llixo.append(round(uniform(1.12,8.55),2))


r = Rocha()
l = Lixo()


pesoPedra = lpedra[randint(0,len(lpedra)-1)]
pesoLixo = llixo[randint(0,len(llixo)-1)]

r.incluirRocha(pesoPedra)
#l.incluirLixoMetal(pesoLixo)
#l.incluirLixoFunk(pesoLixo)


rPeso = r.pesoTotalRochas()
#lPeso = l.pesoTotalLixo()
c = Curiosity(rPeso, 0)
pesoCuriosity = c.pesoCuriosity()

print(pesoCuriosity)
print(type(pesoCuriosity))

#while pesoCuriosity < 9.0:
for i in range(0,5):
    pesoPedra = lpedra[randint(0,len(lpedra)-1)]
    r.incluirRocha(pesoPedra)
    rPeso = r.pesoTotalRochas()
    print(rPeso)
    c = Curiosity(rPeso,0)
    pesoCuriosity = c.pesoCuriosity()
    print(pesoCuriosity)

#balance = r.retirarPedras()
#print(pesoCuriosity)


print('\n CODIGO OK \n')

'''
while pesoCuriosity < 9.0:
    peso = lpedra[randint(0,len(lpedra)-1)]
    trip1.incluirRocha(peso)
    pesoCuriosity = trip1.pesoTotalRochas()
print('\nPeso total de rochas: ', trip1.pesoTotalRochas())
'''
