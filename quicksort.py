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
 
 
 
quicksort(lista)