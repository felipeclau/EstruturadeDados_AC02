def quicksort(l):
    if l:
        left = [x for x in l if x < l[0]]
        right = [x for x in l if x > l[0]]
        if len(left) > 1:
                left = quicksort(left)
        if len(right) > 1:
                right = quicksort(right)
        return left + [l[0]] * l.count(l[0]) + right
    return []


def quicksort2(lista):
    if len(lista) <= 1: return lista
    m = lista[0]
    return quicksort([i for i in lista if i < m]) + \
        [i for i in lista if i == m] + \
        quicksort([i for i in lista if i > m])



print (quicksort2([5,99,2,45,12,234,29,0]))
 
#lista = [6,5,7,10,6,9,1]
#print('Quicksort: ', quicksort(lista))

