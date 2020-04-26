# Disciplina: ESTRUTURA DE DADOS
# Turma: BD3B NOITE
# Nome Alunos: BRUNO BARROCA
#              FELIPE CHIN LAU
#              LETICIA MARQUES
# Professor: JORGE CARLOS VALVERDE REBAZA
# Data entrega: 28/04/2020

''' Pergunta 1: Ranking de Algoritmos de Ordenação'''

# 1.1) Implementação seguindo um esquema de TAD que contenha todos os algoritmos de ordenação como métodos da classe (1 ponto)
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
    
    def insertion_sort(self,lista):
        for i in range(1,len(lista)):
            current = lista[i]
            while i>0 and lista[i-1]>current:
                lista[i] = lista[i-1]
                i = i-1
                lista[i] = current
        return lista
'''
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

# 1.3) Implementação dos algoritmos buble sort e mergesort. Obter resultados de desempenho médio para 
#      M = 10 listas com valores aleatórios de tamanhos N = 1000, N = 10000, N = 100000, N = 1000000 e 
#      N = 10000000. (3 pontos)

from random import randint
import time
N = 1000000                               
tempo = []                              # lista para guardar o tempos de execução do processso, acumulativamente.
print('Processo iniciado!')


#bubble_sort
'''
for i in range(10):  
    lista = [randint(0, N) for i in range(N+1)]
    lista_sorted = Ordenacao()
    bubble = lista_sorted.bubble_sort(lista)
    print("Lista Ordenada com bubble-sort: ")
    tempo.append((time.process_time()))
'''
#merge_sort
'''
for i in range(10):  
    lista = [randint(0, N) for i in range(N+1)]
    lista_sorted = Ordenacao()
    bubble = lista_sorted.merge_sort(lista)
    print("Lista Ordenada com merge-sort: Lista ", i)
    tempo.append((time.process_time()))
'''

# 1.4) Implementação do algoritmo insertion sort. Obter resultados de desempenho médio para M = 10 
#      listas com valores aleatórios de tamanhos N = 1000, N = 10000, N = 100000, N = 1000000 e 
#      N = 10000000. (1 ponto)

#insertion_sort
for i in range(10):  
    lista = [randint(0, N) for i in range(N+1)]
    lista_sorted = Ordenacao()
    bubble = lista_sorted.insertion_sort(lista)
    print("Lista Ordenada com insertion-sort: Lista ", i)
    tempo.append((time.process_time()))

# 1.5) Implementação do algoritmo quicksort. Obter resultados de desempenho médio para M = 10 
#      listas com valores aleatórios de tamanhos N = 1000, N = 10000, N = 100000, N = 1000000 
#      e N = 10000000. (2 pontos)

# quick_sort


# 1.6) Implementação do algoritmo counting sort. Obter resultados de desempenho médio para M = 10 
#      listas com valores aleatórios de tamanhos N = 1000, N = 10000, N = 100000, N = 1000000 e 
#      N = 10000000. (2 pontos)

# counting_sort


print('\n Valor de N = ', N)
print('Tempo de processo: ',tempo)

