def menu():
    print('-='*17)
    print('Menu Sistema Gestor de Postagens')
    print('    1) Criar um post \n    2) Dar likes a um post \n    3) Top posts com mais likes')
    opcao = input('\nDigite uma opção: ')
    print('-='*17)
    return opcao
# função para criar um post
def registroPost(opcao):
    post = []
    if opcao == 1:
        post.append(0)
        return('Post número',len(post),' criado.')

x = menu()
print(registroPost(x))
