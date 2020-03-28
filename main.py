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
        print('{} '.format(indice), end='')
        indice += 1
    print('\n')
    return indice          


# função para dar likes
def darLikes(postagem):
    npost = int(input('Ingresse o número do post ao que você quer dar likes: '))
    nlikes = int(input('Informe o número de likes que vocêr quer atribuir: '))
    postagem[npost] = postagem[npost] + nlikes
    if postagem.index = 0:
        if nlikes <= 10:
            postagem[npost + 1] = postagem[npost + 1] + 1
        else:
            postagem[npost + 1] = postagem[npost + 1] + nlikes //2
    else:
        if nlikes <= 10:
            postagem[npost + 1] = postagem[npost + 1] + 1
            postagem[npost - 1] = postagem[npost - 1] + 1
        else:
            postagem[npost + 1] = postagem[npost + 1] + nlikes //2
            postagem[npost - 1] = postagem[npost - 1] + nlikes //2
            
    return postagem

    
def numeroLikes(postagem):
    indice = ''
    print('Likes: ')
    for i in postagem:
        indice = print('{} '.format(i), end='')
        print('\n')
    return i 

# função sub menu
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


# função top posts com mais likes
    def topLikes(self):
        pass
            

x = menu()
if x == 1:
    registroPost()
if x == 2:
    