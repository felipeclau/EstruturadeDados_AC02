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
    
    def merge_sort(self, lista):                                    # separa a lista em duas, sucessivamente, e depois compara as duas listas, organizando
        if len(lista) < 2:
            return lista
        centro = len(lista) // 2
        lista_L = self.merge_sort(lista[:centro])
        lista_R = self.merge_sort(lista[centro:])
        return self.merge(lista_L, lista_R)


    def merge(self, lista_L, lista_R):                              # separa a lista em duas, comparando as duas.
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

    def quick_sort(self, lista):
        if len(lista) <= 1: return lista
        m = lista[0]
        return self.quick_sort([i for i in lista if i < m]) + \
            [i for i in lista if i == m] + \
            self.quick_sort([i for i in lista if i > m])
    
    def counting_sort(self, lista):
        k = max(lista) + 1                                  # constante para poder cria uma lista com a quantidade de indices do maior valor da lista + 1
        count_list = [0]*(k)                                # lista criada com a quantidade k+1 de indices 
 
        for n in lista:                                     # loop para adicionar o valor de 1 no indice da 'count_list' correspontende ao valor da lista
            count_list[n] = count_list[n] + 1
    
        i=0
        for n in range(len(count_list)):                    # substituindo os valores da lista de acordo com o indices na lista 'count_list'
            while count_list[n] > 0:
                lista[i] = n
                i+=1
                count_list[n] -= 1



# # # # #  EXECUÇÃO PROGRAMA # # # # #  
''' 
    A execução do programa deve ser feita retirando as aspas triplas para execução dos algoritmos. Isso foi 
    necessário para que não haja execução dos 5 algoritmos, cada um executando um loop de 10 ciclos. Dependendo
    do algoritmo isso pode tomar muito tempo, podendo até não ser finalizado em várias horas. Portanto, execute
    com moderação.
    O valor de N foi alterado para cada execução.

'''
# 1.3) Implementação dos algoritmos buble sort e mergesort. Obter resultados de desempenho médio para 
#      M = 10 listas com valores aleatórios de tamanhos N = 1000, N = 10000, N = 100000, N = 1000000 e 
#      N = 10000000. (3 pontos)

from random import randint
import time
#N = 1000
#N = 10000
#N = 100000
#N = 1000000
#N = 10000000                              
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
    merge = lista_sorted.merge_sort(lista)
    print("Lista Ordenada com merge-sort: Lista ", i)
    tempo.append((time.process_time()))
'''

# 1.4) Implementação do algoritmo insertion sort. Obter resultados de desempenho médio para M = 10 
#      listas com valores aleatórios de tamanhos N = 1000, N = 10000, N = 100000, N = 1000000 e 
#      N = 10000000. (1 ponto)

#insertion_sort
'''
for i in range(10):  
    lista = [randint(0, N) for i in range(N+1)]
    lista_sorted = Ordenacao()
    insertion = lista_sorted.insertion_sort(lista)
    print("Lista Ordenada com insertion-sort: Lista ", i)
    tempo.append((time.process_time()))
'''

# 1.5) Implementação do algoritmo quicksort. Obter resultados de desempenho médio para M = 10 
#      listas com valores aleatórios de tamanhos N = 1000, N = 10000, N = 100000, N = 1000000 
#      e N = 10000000. (2 pontos)

# quick_sort
'''
for i in range(10):  
    lista = [randint(0, N) for i in range(N+1)]
    lista_sorted = Ordenacao()
    quick = lista_sorted.quick_sort(lista)
    print("Lista Ordenada com quick-sort: Lista ", i)
    tempo.append((time.process_time()))
'''
<<<<<<< HEAD

=======
>>>>>>> a570b5884c04ee74ed47494bac669ef0071418f5

# 1.6) Implementação do algoritmo counting sort. Obter resultados de desempenho médio para M = 10 
#      listas com valores aleatórios de tamanhos N = 1000, N = 10000, N = 100000, N = 1000000 e 
#      N = 10000000. (2 pontos)

# counting_sort

for i in range(10):  
    lista = [randint(0, N) for i in range(N+1)]
    lista_sorted = Ordenacao()
    quick = lista_sorted.counting_sort(lista)
    print("Lista Ordenada com counting-sort: Lista ", i)
    tempo.append((time.process_time()))

print('\n Valor de N = ', N)
print('Tempo de processo: ',tempo)

