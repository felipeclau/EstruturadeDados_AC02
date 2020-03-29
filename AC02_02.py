# Disciplina: ESTRUTURA DE DADOS
# Turma: BD3B NOITE
# Nome Aluno: FELIPE CHIN LAU
# Professor: JORGE CARLOS VALVERDE REBAZA
# Data entrega: 31/03/2020

'''
PERGUNTA 2: Rover Curiosity
'''
class Rocha:
    def __init__(self,lista):
        self.lista = lista

    def listaPedra(self, tamanho, peso):
        pass




# SIMULAÇÃO
from random import randint, uniform

# lista de pedras:
lpedra = []                             # lista de pedras
npedra = randint(30,120)                # número aleatório entre 30 e 120 de elementos na lista pedra
for i in range(0,npedra):               # inserção do peso das pedras dentro de um range.
    lpedra.append(round(uniform(0.5,14.2),2))

# pilha de lixo:
llixo = []                             # lista de lixos.
nlixo = randint(30,120)                # número aleatório entre 30 e 120 de elementos na pilha lixo
for i in range(0,nlixo):              # inserção do pedo do lixo dentro de um range.
    lpedra.append(round(uniform(1.12,8.55),2))

peso = sum(lpedra) + sum(llixo)

