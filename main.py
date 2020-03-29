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
    print('Post número {} criado. \n'.format(len(postagem)))
    print('A lista de postagens é a seguinte: \n')
    
    indice = 0
    print('Índice: ', end='')
    while indice < len(postagem):
        print('{} '.format(indice), end=' ')     # printando os índices em lista.
        indice += 1
    print('\n')
    
    likes = ''
    print('Likes: ', end='')
    for i in postagem:
        likes = print(' {} '.format(i), end='')   # printando os likes em linha.
    print('\n')   

# função para dar likes
def darLikes(postagem):
    if len(postagem) == 0:
        print('Não há posts para dar like.\n')
    else:
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

        print('\n')
        indice = 0
        print('Índice: ', end='')
        while indice < len(postagem):
            print('{} '.format(indice), end=' ')     # printando os índices em lista.
            indice += 1
        print('\n')
        
        likes = ''
        print('Likes: ', end='')
        for i in postagem:
            likes = print(' {} '.format(i), end='')   # printando os likes em linha.
        print('\n')  
    

# função top posts com mais likes
def topLikes(postagem):
    if len(postagem) == 0:
        print('Não ha postagens realizadas.\n')
    else:
        print('O top-3 posts com mais likes são: \n') 
        print('Top:     1  2  3')       # cabeçalho
        copialista = postagem[:]        # cópia da lista postagem, para fazer comparações.
        top3 = []                       #lista vazia para colocar o top 3.
        
        for i in range(1,4):            # loop para pegar os 3 índices com maiores valores.
            imaior = 0                  # maior índice
            maior = max(copialista)     # variável para maior valor da lista copiada
            for valor in postagem:      # loop para pegar o maior valor na lista original
                if valor == maior:
                    top3.append(postagem.index(valor))                # inclusão do índice de valor maior na lista top3.
            del(copialista[copialista.index(maior)])                  # exclusão deste valor na lista copiada, para a próxima comparação entre a lista original e a cópia.
            
        print('Índice: {}'.format(top3))
        print('Likes: {}' .format(sorted(postagem, reverse=True)))    # ordenação dos valores descrescentes da lista, sem alterar a lista.


# função para retornar ao menu
def retornar():
    resposta = str(input('Aperte R para voltar: ')).upper().strip()
    if resposta == 'R':
        menu()
    else:
        print('Programa finalizado')


postagem = []

while True:
    opc = menu()
    if opc == 1:
        registroPost(postagem)
    elif opc == 2:
        darLikes(postagem)
    elif opc == 3:
        topLikes(postagem)
    else:
        opc = menu()
