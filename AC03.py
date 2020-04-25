# Disciplina: ESTRUTURA DE DADOS
# Turma: BD3B NOITE
# Nome Alunos: BRUNO BARROCA
#              FELIPE CHIN LAU
#              LETICIA MARQUES
# Professor: JORGE CARLOS VALVERDE REBAZA
# Data entrega: 28/04/2020

''' Pergunta 1: Ranking de Algoritmos de Ordenação'''

class Ordenacao:
    def __init__(self):
        pass
    
    def merge_sort(self, lista):
        if len(lista) < 2:
            return lista
        centro = len(lista) // 2
        lista_L = self.merge_sort(lista[:centro])
        lista_R = self.merge_sort(lista[centro:])
        return self.merge(lista_L, lista_R)


    def merge(self, lista_L, lista_R):
        if len(lista_L) == 0:
            return lista_R
        if len(lista_R) == 0:
            return lista_L
        result = []
        index_L = index_R = 0
        while len(result) < len(lista_L) + len(lista_R):
            if lista_L[index_L] <= lista_R[index_R]:
                result.append(lista_L[index_L])
                index_L += 1
            else:
                result.append(lista_R[index_R])
                index_R += 1
            if index_R == len(lista_R):
                result += lista_L[index_L:]
                break
            if index_L == len(lista_L):
                result += lista_R[index_R:]
                break
        return result
    
    def bubble_sort(self, lista):
        n = len(lista)
        for i in range(n):
            ordenado = True 
            for j in range(n - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    ordenado = False
            if ordenado:
                break
        return lista
    '''
    def insertion_sort(self, lista):
        for i in range(1,len(lista)):
        #element to be compared
            current = lista[i]

       #comparing the current element with the sorted portion and swapping
        while i>0 and lista[i-1]>current:
            lista[i] = lista[i-1]
            i = i-1
            lista[i] = current

        return lista

    def quick_sort(self, lista):
    	if l:
		    left = [x for x in l if x < l[0]]
		    right = [x for x in l if x > l[0]]
		if len(left) > 1:
		    left = quicksort(left)
		if len(right) > 1:
			right = quicksort(right)
		return left + [l[0]] * l.count(l[0]) + right
	    return []
 '''
 
 
# EXECUÇÃO PROGRAMA

from random import randint
import time

N = 100000
tempo = []

#bubble_sort
for i in range(10):  
    lista = [randint(0, N) for i in range(N+1)]
    print("Lista inicial: ")
    print(lista)
    lista_sorted = Ordenacao()
    bubble = lista_sorted.bubble_sort(lista)
    print("Lista Ordenada com bubble-sort: ")
    t = time.process_time()
    tempo.append((time.process_time()))

print('\n Valor de N = ', N)
print('Tempo de processo: ',tempo)

