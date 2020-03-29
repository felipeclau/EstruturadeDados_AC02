def menu():
    print('-='*17)
    print('Menu Sistema Gestor de Postagens')
    print('    1) Criar um post \n    2) Dar likes a um post \n    3) Top posts com mais likes')
    opcao = int(input('\nDigite uma opção: '))
    print('-='*17)
    return opcao
# função para criar um post
def registroPost(postagem):
        postagem.append(0)
        print('Post número {} criado.'.format(len(postagem)))

# função com o resultado após a execução de uma das opções do menu.
def numeroPostagens(postagem):
    indice = 0
    print('Índice: ', end='')
    while indice < len(postagem):
        print('{} '.format(indice), end='')     # printando os índices em lista.
        indice += 1
    print('\n')
    return indice          


# função para dar likes
def darLikes(postagem):
    npost = int(input('Ingresse o número do post ao que você quer dar likes: ')) 
    if npost >= len(postagem):              # se o post for maior que a lista da postagem, escolhe um número aleatorio dentro do range da lista.
        from random import randint
        npost = randint(0,len(postagem)-1)
    nlikes = int(input('Informe o número de likes que vocêr quer atribuir: '))
    postagem[npost] = postagem[npost] + nlikes      # altera o valor da lista.
    if npost == 0 or npost == len(postagem) - 1:
        if npost == 0:
            if nlikes <= 10:
                postagem[npost + 1] = postagem[npost + 1] + 1
            else:
                postagem[npost + 1] = postagem[npost + 1] + nlikes //2
        if npost == len(postagem) - 1:
            if nlikes <= 10:
                postagem[npost - 1] = postagem[npost - 1] + 1
            else:
                postagem[npost - 1] = postagem[npost - 1] + nlikes //2
    else:
        if nlikes <= 10:
            postagem[npost + 1] = postagem[npost + 1] + 1
            postagem[npost - 1] = postagem[npost - 1] + 1
        else:
            postagem[npost + 1] = postagem[npost + 1] + nlikes //2
            postagem[npost - 1] = postagem[npost - 1] + nlikes //2

    return postagem

# função para imprimir o resultado das likes.
def numeroLikes(postagem):
    indice = ''
    print('Likes: ', end='')
    for i in postagem:
        indice = print('{} '.format(i), end='')   # printando os likes em linha.
    print('\n')
    return i 

# função top posts com mais likes
def topLikes(postagem):
    print('Top:     1    2    3') # cabeçalho
    ordemIndice = ''
    lista = []                      #lista vazia para colocar o top 3.
    lista.append(postagem.index([max(postagem)))  # índice com o maior valor da lista

    print('Índice: ')
    print('Likes: {}' .format(sorted(postagem, reverse=True)))    # ordenação em ordem descrescente da lista, sem alterar a lista.


# função sub menu

'''
def submenu():
    print('A lista de postagens é o seguinte: {}', postagem)
    print('Índice: \nLikes: ')
    opc = ''
    while True:
        opc = str(input('Aperta R para voltar ou S para sair: ')).upper().strip()
        if opc !='R' or opc != 'S':
            if opc == 'R':
                menu()
                break
            if opc == 'S':
                break
            else:
                print('Opção inválida!')
    pass
'''