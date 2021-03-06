# -*- coding: utf-8 -*-

from Grafo import Grafo
import os

# ---------------------- Definição dos Menus ---------------------- #
def print_menu_arquivo():
    print ("\nDigite o nome do arquivo a ser lido:")

def print_menu_estrutura_dados():
    print (67 * "-")
    print ("\nEscolha uma Estrutura de Dados para representar o grafo\n")
    print ("1. M.A.")
    print ("2. M.I.")
    print ("3. L.A.")
    print ("4. Sair\n")

def print_menu_geral():
    print ("\n" + 67 * "-")
    print ("\nSelecione a operacao para executar no grafo:\n")
    print("1.  Imprimir o grafo")
    print ("2.  ehVizinho")
    print ("3.  obtemVizinhos")
    print ("4.  Deletar uma Aresta")
    print ("5.  ehPredecessor")
    print ("6.  ehSucessor")
    print ("7.  obtemSucessores")
    print ("8.  obtemPredecessores")
    print ("9.  Deletar um vertice")
    print("10. Conversoes")
    print ("11. Sair\n")

# Variáveis auxiliares para os menus
sair = False
loop = False

# ---------------------- Menu de leitura do arquivo ---------------------- #

loop=True      
  
while loop:
    print_menu_arquivo()
    arquivo = raw_input()
    path = None
   
    # Navega pela pasta a procura do arquivo
    for root, dirs, files in os.walk("../instances"):
        if path is None: # Evita encontrar dois arquivos com o mesmo nome
            for file in files:
                if arquivo in file:
                    print("\nArquivo encontrado!")
                    path = os.path.join(root, file)
                    print("Caminho: " + path +"\n")
                    loop = False
                    break # Evita encontrar dois arquivos com o mesmo nome
    
    if path is None:
        print("\nArquivo nao encontrado! Certifique-se de estar rodando o sistema a partir da pasta raiz 'source'!\n")

# ---------------------- Menu de Estrutura de Dados ---------------------- #

loop=True

while loop: 

    print_menu_estrutura_dados()
    tipo_estrutura = input("Digite sua escolha [1-4]: ")
    tipo_estrutura = int(tipo_estrutura)

    def cria_grafo():
        global grafo # Torna o grafo acessível fora desse contexto
        grafo = Grafo(tipo_estrutura, path)
        grafo = grafo._cria()
        print(grafo)

    if tipo_estrutura == 1:     
        print ("\nMatriz de Adjacencia selecionada!\n")
        cria_grafo()
        loop = False

    elif tipo_estrutura == 2:
        print ("\nMatriz de Incidencia selecionada!\n")
        cria_grafo()
        loop = False

    elif tipo_estrutura == 3:
        print ("\nLista de Adjacencia selecionada!\n")
        cria_grafo()
        loop = False

    elif tipo_estrutura == 4:
        print ("Saindo...")
        sair = True
        loop = False

    else:
        print ("\nOpcao escolhida invalida!\n")

# ------------------------------ Menu Geral ------------------------------ #

loop=True

while loop and not sair:
    print_menu_geral()
    escolha = input("Digite sua escolha [1-X]: ") # Editar o X para o número final de opções
    escolha = int(escolha)

    if escolha == 1:

        print("\n")     
        print (grafo)

    elif escolha == 2:

        print ("\n" + 67 * "-")
        print ("\nDigite os vertices u,v para verificar se o vertice v eh vizinho de u")

        parVertices = input("u,v: ")
        parVertices = parVertices.split(",")
        u = parVertices[0]
        v = parVertices[1]
        print(grafo._ehVizinho(u,v))

    elif escolha == 3:
        print ("\n" + 67 * "-")
        print ("\nDigite um vertice para verificar seus vizinhos")
        vertice = input("u: ")
        print(grafo._obtemVizinhos(vertice))
    
    elif escolha == 4:

        print ("\n" + 67 * "-")
        print ("\nDigite a aresta que deseja remover")

        aresta = input("u,v: ")
        aresta = aresta.split(",")
        u = aresta[0]
        v = aresta[1]
        resultado = grafo._deletaAresta(u,v)

        if resultado == True:
            print("\nAresta removida com sucesso!\n")
            print(grafo)
        else:
            print ("\nA aresta digitada nao existe!")

    elif escolha == 5:

        print ("\n" + 67 * "-")

        if grafo._direcionado == False:
            print ("Grafo nao direcionado. Impossivel realizar operacao!")
        else:
            print ("\nDigite u,v para checar se v eh predecessor de u (v->u)")
            vertices = input("u,v: ")
            vertices = vertices.split(",")
            u = vertices[0]
            v = vertices[1]
            print(grafo._ehPredecessor(u,v))

    elif escolha == 6:

        print ("\n" + 67 * "-")

        if grafo._direcionado == False:
            print ("Grafo nao direcionado. Impossivel realizar operacao!")
        else:
            print ("\nDigite u,v para checar se v eh sucessor de u (v<-u)")
            vertices = input("u,v: ")
            vertices = vertices.split(",")
            u = vertices[0]
            v = vertices[1]
            print(grafo._ehSucessor(u,v))

    elif escolha == 7:

        print ("\n" + 67 * "-")

        if grafo._direcionado == False:
            print ("Grafo nao direcionado. Impossivel realizar operacao!")
        else:
            print ("\nDigite um vertice u para obter o conjunto de sucessores desse vertice")
            u = input("u: ")
            print(grafo._obtemSucessores(u))

    elif escolha == 8:

        print ("\n" + 67 * "-")
        if grafo._direcionado == False:
            print ("Grafo nao direcionado. Impossivel realizar operacao!")
        else:
            print ("\nDigite um vertice u para obter o conjunto de predecessores desse vertice")
            u = input("u: ")
            print(grafo._obtemPredecessores(u))

    elif escolha == 9:

        print ("\n" + 67 * "-")
        print ("\nDigite o vertice que deseja remover")
        u = input("u:")

        try:
            grafo._deletaVertice(u)
            print("\nVertice removido com sucesso!\n")
            print(grafo)

        except Exception as e: 
            print(e)

    elif escolha == 10:

        print ("\n" + 67 * "-")
        print ("\nEscolha uma das opcoes para efetuar a conversao:")

        # 1 - M.A. | 2 - M.I. | 3 - L.A.

        if (tipo_estrutura == 1): #M.A.
            print ("\n1.Converter a M.A. para L.A.")
            print ("2.Converter a M.A. para M.I.")
            u = input("\nDigite sua escolha [1-2]:")
            u = int(u)

            if (u != 1 and u != 2):
                print("Opcao inexistente!")
            else:
                try:    
                    grafo._efetuaConversao(u)
                except Exception as e: 
                    print(e)

        elif (tipo_estrutura == 2): #M.I.
            print ("\n1.Converter a M.I. para L.A.")
            print ("2.Converter a M.I. para M.A.")
            u = input("\nDigite sua escolha [1-2]:")
            u = int(u)

            if (u != 1 and u != 2):
                print("Opcao inexistente!")
            else:
                try:    
                    grafo._efetuaConversao(u)
                except Exception as e: 
                    print(e)

        elif (tipo_estrutura == 3): #L.A.
            print ("\n1.Converter a L.A. para M.A.")
            print ("2.Converter a L.A. para M.I.")
            u = input("\nDigite sua escolha [1-2]:")
            u = int(u)

            if (u != 1 and u != 2):
                print("Opcao inexistente!")
            else:
                try:    
                    grafo._efetuaConversao(u)
                except Exception as e: 
                    print(e)

        else:
            print("Impossivel realizar operacao!")

    elif escolha == 11:
        print ("Saindo...")
        sair = True
        loop = False

    else:
        print ("\nOpcao escolhida invalida!\n")