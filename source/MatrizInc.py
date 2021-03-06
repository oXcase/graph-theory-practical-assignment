# -*- coding: utf-8 -*-
from Aresta import Aresta

# Representação de infinito
INF = 1E8

class MatrizInc(object): 
    
    ''' 
    Construtor da classe
    '''
    def __init__(self, direcionado):

        self.__M = [] # Cria, inicialmente, uma matriz sem elementos

        # Numero de vertices (Membro privado da classe)
        self.__nVertices = 0

        # Numero de arestas (Membro privado da classe)
        self.__nArestas = 0 
        
        # Dicionario que contem o nome do vertice como chave e 
        # como valor, sua posicao na lista
        self.__posicoes = {} 
        
        # Dicionario que contem a posicao do vertice na matriz como chave 
        # e como valor, o nome do vertice
        self.__vertices = {}
        self._direcionado = direcionado
    
    ''' 
    Destrutor da classe
    ''' 
    def __del__(self):  
        del self.__M

    ''' 
    Impressão da matriz de incidencia
    ''' 
    def __str__(self):
        saida = "V = { "
        for v in self.__posicoes:
            saida += v + " "
        saida += "}\n\n"

        saida += "Matriz de incidencia\n\n"
        for i in range(self.__nArestas):
            for j in range(self.__nVertices):
                saida += str(self.__M[i][j]) + " "
            saida += "\n"
        saida += "\n"
        return saida

    '''
    Dada uma posição da matriz, retorna um vertice (neste caso, 
    optei pelo nome)
    '''
    def _obtemVertice(self, pos):
        return self.__vertices[pos]

    ''' 
    Dado um vértice, retorna sua posição relativa na matriz
    ''' 
    def _obtemPosicao(self, u):
        try:
            return self.__posicoes[str(u)]
        except:
            return -1

    '''
    Retorna os vizinhos do vertice u (retorna sua posicao 
    relativa na matriz)
    Em grafos direcionados serão considerados vizinhos apenas
    os sucessores diretos do vértice. (Será desconsiderada a relação
    negativa entre os vértices nas arestas)
    '''
    def _obtemVizinhos(self, u):

        pos_u = self._obtemPosicao(str(u))

        # Se for diferente significa que o vértice não existe
        if pos_u >= 0:
            lista = []
            for i in range(self.__nArestas):
                for v in range(self.__nVertices):
                    if(pos_u != v and self.__M[i][pos_u] > 0 and 
                    self.__M[i][pos_u] != INF and self.__M[i][v] != 0 
                    and self.__M[i][v] != INF):
                        lista.append(self.__vertices[v])
                        break
            return lista

        else:
            return []

    '''
    Verifica se o vertice v é vizinho de u.
    Em grafos direcionados serão considerados vizinhos apenas
    os sucessores diretos do vértice. (Será desconsiderada a relação
    negativa entre os vértices nas arestas)
    '''
    def _ehVizinho(self, u, v):
        # Obtenção da posição relativa do vértice u
        pos_u = self._obtemPosicao(u) 
        # Obtenção da posição relativa do vértice v
        pos_v = self._obtemPosicao(v) 

        if(pos_u >= 0 and pos_v >= 0):
            for i in range(self.__nArestas):
                if(self.__M[i][pos_u] > 0 and self.__M[i][pos_u] != INF
                  and self.__M[i][pos_v] != 0 and self.__M[i][pos_v] != INF):
                    return True

        # Caso pos_u == -1 ou pos_v == -1
        return False

    ''' 
    Remove uma aresta (u,v) do grafo
    ''' 
    def _deletaAresta(self, u, v):

        for index,aresta in enumerate(self._obtemArestas()):
            if (aresta._obtemVerticeU() == u 
             and aresta._obtemVerticeV() == v):
            
                self.__M.pop(index)
                self.__nArestas = self.__nArestas - 1

                return True

        return False
    
    '''
    Recebe dois vértices u e v como parâmetros 
    e retorna true se v é predecessor de u (v aponta pra u)
    Apenas para grafos direcionados.
    '''
    def _ehPredecessor(self,u,v):
        
        for aresta in self._obtemArestas():
            if (aresta._obtemVerticeU() == v 
             and aresta._obtemVerticeV() == u):
                return True
        
        return False

    '''
    Recebe dois vértices u e v como parâmetros 
    e retorna true se v é sucessor de u (u aponta pra v)
    Apenas para grafos direcionados.
    Serão considerados sucessores todos os vizinhos do vértice.
    '''
    def _ehSucessor(self,u,v):

        for i in range(self.__nArestas):
            
            # Verifica existencia dos vértices
            try:
                self.__M[i][int(u)]
                self.__M[i][int(v)]
            except:
                return False

            if (self.__M[i][int(u)] and self.__M[i][int(v)] < 0) and self._direcionado:
                return True

        return False


    '''
    Recebe um vértice u como parâmetro e retorna
    o conjunto de sucessores desse vértice
    (Todos os vértices dos quais u aponta)
    Apenas para grafos direcionados.
    Serão considerados sucessores todos os vizinhos do vértice.
    '''
    def _obtemSucessores(self,u):

        sucessores = []

        for aresta in self._obtemArestas():
            if aresta._obtemAresta()[0] == u:
                sucessores.append(self._obtemVertice(int(aresta._obtemAresta()[1])))

        return sucessores

    '''
    Recebe um vértice u como parâmetro e retorna
    o conjunto de predecessores desse vértice
    (Todos os vértices que apontam para u)
    Apenas para grafos direcionados.
    '''
    def _obtemPredecessores(self,u):             
        
        predecessores = []

        for aresta in self._obtemArestas():
            if (aresta._obtemVerticeV() == u):
                vertice = aresta._obtemVerticeU()
                predecessores.append(vertice)

        return predecessores
    
    '''
    Deleta um vértice do grafo e as arestas 
    incidentes a ele (por consequência)
    '''
    def _deletaVertice(self,u):        
        raise Exception("\nOperacao ainda nao implementada!")  # Ainda não implementado

    ''' 
    Retorna a lista de arestas do grafo
    ''' 
    def _obtemArestas(self):
        listaArestas = []
        for i in range(self.__nArestas):
            u = v = -1
            for j in range(self.__nVertices):
                if(self.__M[i][j] != 0 
                   and self.__M[i][j] != INF):
                    # Armazenando os pares u,v
                    if(u == -1):
                        u = j
                      
                    else:
                        v = j
            if(u >= 0 and v >= 0):
                if((self.__M[i][u] >= 0 and self.__M[i][v] < 0) or (self.__M[i][u] >= 0 and self.__M[i][v] >= 0)
                  or (self.__M[i][u] < 0 and self.__M[i][v] < 0)):
                    aresta = Aresta(self.__vertices[u], self.__vertices[v], self.__M[i][u])
                
                elif(self.__M[i][u] < 0 and self.__M[i][v] >= 0):
                    aresta = Aresta(self.__vertices[v], self.__vertices[u], self.__M[i][v])
              
            listaArestas.append(aresta)
              
        return listaArestas

    '''
    Adiciona um novo elemento ao grafo
    '''
    def _add(self, u, v = None, peso = 1):
        if(u == None):
            return

        vertice_u = str(u)
        # Se v for None, então verificamos a inserção de um vértice
        if(v == None):
            # Se u não foi inserido, vamos inserí-lo
            if(not (vertice_u in self.__posicoes)):
                self.__criaVertice(u)

        else:
            vertice_v = str(v)
            # Se u e v não são vizinhos, cria a ligação entre eles
            if(not(self._ehVizinho(u, v))):
                self.__criaAresta(u, v, peso)

                # No caso de grafos direcionados, modifica a ligação dos vértices
                # na aresta para negativa, na posição contrária ao direcionamento da mesma.
                if(self._direcionado == True):
                    self.__M[self.__nArestas][self._obtemPosicao(v)] = -1*self.__M[self.__nArestas][self._obtemPosicao(v)]
                
                # Aumenta o numero de arestas
                self.__nArestas = self.__nArestas + 1 
    
    '''
    Cria uma aresta de ligação entre os vértices u e v, 
    dado um peso (1, por default)
    '''
    def __criaAresta(self, u, v, peso = 1):
        # Cria a nova aresta
        self.__M.append([])

        # Zerando as colunas da nova aresta
        for i in range(self.__nVertices):            
            self.__M[self.__nArestas].append(0)

        # Obtenção da posição relativa do vértice u
        pos_u = self._obtemPosicao(u) 
        # Obtenção da posição relativa do vértice v
        pos_v = self._obtemPosicao(v) 
        
        # Ligação dos vértices u e v, feita na ida e na volta
        if(pos_u >= 0 and pos_v >= 0):
            self.__M[self.__nArestas][pos_u] = peso
            self.__M[self.__nArestas][pos_v] = peso
    
    ''' 
    Criacao de um vertice para a matriz
    ''' 
    def __criaVertice(self, u):            
        self.__nVertices += 1
        # for linhaM in self.__M:
        #     self.linhaM.append(0)
        self.__posicoes[str(u)] = self.__nVertices - 1
        self.__vertices[self.__nVertices - 1] = str(u)

    ''' 
    Efetua conversão de tipo de estrutura
    ''' 
    def _efetuaConversao(self, tipo_estrutura):
        raise Exception("\nOperacao ainda nao implementada!")  # Ainda não implementado