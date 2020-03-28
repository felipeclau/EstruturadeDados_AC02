# Disciplina: ESTRUTURA DE DADOS
# Turma: BD3B NOITE
# Nome Aluno: FELIPE CHIN LAU
# Professor: JORGE CARLOS VALVERDE REBAZA
# Data entrega: 31/03/2020

'''
PERGUNTA 1: Likes de Postagens em Redes Sociais
'''


class Post:
    def __init__(self, indice, like):
        self.indice = indice
        self.like = like
    
# função para criar um post
    def registroPost(self, opcao):
        post = []
        if opcao == 1:
            post.append(0)
            print('Post número {} criado.'.format(len(post)))
            print('A lista de postagens é a seguinte:')

# função com o resultado após a execução de uma das opções do menu.
    def resultado(self, indice, likes):
            self.indice()
            self.likes()
            pass
        
# função para dar likes
    def darLikes(self):
        pass
    
# função top posts com mais likes
    def topLikes(self):
        pass
            


# função para criar um menu.
def menu(self):
    print('-='*17)
    print('Menu Sistema Gestor de Postagens')
    print('    1) Criar um post \n    2) Dar likes a um post \n    3) Top posts com mais likes')
    opcao = input('\nDigite uma opção: ')
    print('-='*17)
    return opcao