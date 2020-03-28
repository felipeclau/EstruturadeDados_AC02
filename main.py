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
    def darLikes(postagem, indicepostagem):
        postagem[indicepostagem] = postagem[indicepostagem] + 1
        
    
def numeroLikes(postagem):
    likes = ''
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
            
