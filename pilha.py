#exercicio da semana 5

class Quadrado:
    #construtor
    def __init__(self, lado):
        self.lado = lado

    #metodos
    def getLado(self):
        return self.lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return self.lado * 4

    def imprimir(self):
        print("Lado = ", self.lado, " A = ", self.area(), "  P = ", self.perimetro())


class Circunferencia:
    #construtor
    def __init__(self, radio):
        self.radio = radio
        self.PI = 3.141596
    
    #metodos
    def getRadio(self):
        return self.radio

    def area(self):
        return self.PI * self.radio * self.radio 

    def perimetro(self):
        return 2 * self.PI * self.radio

    def imprimir(self):
        print("Radio = ", self.radio, " A = ", self.area(), "  P = ", self.perimetro())


class Pilha:
    #construtor
    def __init__(self):
        self.pilha = [] 

    #metodos
    def push(self, valor):
        self.pilha.append(valor)

    def pop(self):
        return self.pilha.pop()

    def isEmpty(self):
        if len(self.pilha) == 0:
            return True
        return False

    def size(self):
        return len(self.pilha)

    def top(self):
        indice_topo = len(self.pilha) - 1
        return self.pilha[indice_topo] 

    def imprimir_c(self):
        indice = len(self.pilha) - 1
        
        while indice >= 0:
            self.pilha[indice].imprimir()
            indice = indice - 1



class Figuras:
    #construtor
    def __init__(self):
        self.lista_quadrados = []
        self.pilha_circulos  = Pilha()

    #metodos
    def setQuadrado(self, quadrado):
        self.lista_quadrados.append(quadrado)

    def setCircunferencia(self, circunferencia):
        self.pilha_circulos.push(circunferencia)

    def imprimir(self):
        print("\nQuadrados: ")
        for q in self.lista_quadrados:
            q.imprimir()

        print("\nCircunferencias: ")
        self.pilha_circulos.imprimir_c()



    '''
    Busca de quadrados de acordo à área, isto é, retornar todos os
    quadrados que tenham uma área menor o igual a um determinado
    valor
    '''
    def busca_quadrados(self, area_buscado):
        l_quads_solucao = []
        for quadrado in self.lista_quadrados:
            if quadrado.area() <= area_buscado:
                l_quads_solucao.append(quadrado)
        return l_quads_solucao

    '''
    Desempilhar circunferências até ter no topo da pilha uma
    circunferência com uma área menor o igual a um determinado valor.
    Caso não encontrar uma circunferência que cumpra essa condição, a
    pilha de circunferência deve ser totalmente restaurada.
    '''
    def busca_circunferencias(self, area_buscado):
        cirsc_temp = [] #para salvar as circunferencias que sao desempilhadas, caso precise recuperar a pilha

        while self.pilha_circulos.isEmpty() == False:
            circulo_do_topo = self.pilha_circulos.pop()
            
            if circulo_do_topo.area() <= area_buscado:
                self.setCircunferencia(circulo_do_topo)
                return True 

            cirsc_temp.append(circulo_do_topo) #sempre salvo na lista caso precise recuperar

        #confiro se a lista contendo a solucao estiver vazia, quer
        #dizer que não tive resposta e, por tanto, devo recuperar a pilha        
        for circunferencia in cirsc_temp:
            self.setCircunferencia(circunferencia)

        return False 

#testando
q1 = Quadrado(5)
q2 = Quadrado(7)
q3 = Quadrado(11)

c1 = Circunferencia(2)
c2 = Circunferencia(8)
c3 = Circunferencia(6)

print('VALOR DE c1 É:', c1)

figs = Figuras()
figs.setQuadrado(q1)
figs.setQuadrado(q2)
figs.setQuadrado(q3)
figs.setCircunferencia(c1)
figs.setCircunferencia(c2)
figs.setCircunferencia(c3)
figs.imprimir()

print('VALOR DE fig.setCircunferencia É:', figs.setCircunferencia(c1))
qs = figs.busca_quadrados(50)
print("Os quadrados com area menor a 50 sao: ")
for q in qs:
    q.imprimir()

flag = figs.busca_circunferencias(15)
print("As circunferencias com area menor a 15 sao")
if flag == False:
    print("Nao ha circunferencia com essa condicao")
else:
    print("A pilha foi atualizada")
    figs.imprimir()


flag = figs.busca_circunferencias(8)
print("As circunferencias com area menor a 8 sao")
if flag == False:
    print("Nao ha circunferencia com essa condicao")
else:
    print("A pilha foi atualizada")
    figs.imprimir()
