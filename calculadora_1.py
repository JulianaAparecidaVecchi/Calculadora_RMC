import time
import numpy as np
import matplotlib.pyplot as plt



def linha():
    print(80*"-")

def sleep():
    time.sleep(1)

def menu():
    linha()
    print("Calculadora - Escolha sua operação aritmética!")
    linha_menu()
    print("1 - Conjuntos numéricos")
    print("2 - Funções de segundo grau")
    print("3 - Funções exponenciais")
    print("4 - Matrizes")
    print("0 - Sair da calculadora")
    linha_menu()

def linha_menu():
    print(20*'=')

def escolha_opcao(): 
    escolha = int(input("Digite o número da opção desejada!\n"))
    return escolha       

def pedir_conjunto(nomeconjunto): 
    conjunto = set(input(f"Digite o conjunto {nomeconjunto}!\n "))
    return conjunto  

def calcular_diferença(conjuntoA,conjuntoB):
    diferenca=conjuntoA - conjuntoB
    return diferenca

def calcular_interseccao(conjuntoA,conjuntoB):
    interseccao = conjuntoA & conjuntoB
    return interseccao

def calcular_uniao(conjuntoA,conjuntoB):
    uniao = conjuntoA | conjuntoB
    return uniao

def escolha_1():
    global menu, escolha_opcao
    linha()
    print("Perfeito, opção (conjuntos numérios) selecionada!")
    linha()
    print("Informe seus conjuntos!")
    print('OBS:Digite os elementos entre espaços')
    conj1 = pedir_conjunto("A")
    conj2 = pedir_conjunto("B")
    while True:
            linha_menu()
            print("A - Verificar se A é subconjunto próprio de B")
            print("B - Realizar operação de União")
            print("C - Calcular intersecção")
            print("D - Calcular diferença")
            print("0 - Voltar")
            linha_menu()
            escolhaLetra1 = str(input("Digite a letra da opção desejada!\n"))
            linha()
            if escolhaLetra1 == '0':
                print("Voltando...")
                sleep()
                break

            if escolhaLetra1.lower() == 'a':
                if conj1 <= conj2 and conj1 != conj2:
                    linha()
                    print("A é um subconjunto próprio de B")
                    linha()
                    sleep()
                elif conj2 <= conj1 and conj2 != conj1:
                    linha()
                    print("A não é um subconjunto próprio de B, mas B é um subconjunto próprio de A")
                    linha()
                    sleep()
                else:
                    linha()
                    print("A não é um subconjunto próprio de B")
                    linha()
                    sleep()

            elif escolhaLetra1.lower() == 'b':
                uniao =  calcular_uniao(conj1,conj2)
                linha()
                print(f" A união é: {uniao}")
                linha()
                sleep()
            elif escolhaLetra1.lower() == 'c':
                interseccao = calcular_interseccao(conj1,conj2)
                linha()
                print(f" A intersecção é: {interseccao}")
                linha()
                sleep()
            elif escolhaLetra1.lower() == 'd':
                linha()
                diferenca = calcular_diferença(conj1,conj2)
                print(f"A diferença é: {diferenca}")
                linha()
                sleep()
            else:
                print("Opção inválida. Tente novamente.")
                continue

def calcular_segundo_grau(a, b, c, x):
    return a * x ** 2 + b * x + c

def definir_eixox():
    x=np.arange(-100,101,1)
    #vai de -100 até 100 de um em um
    return x

def gerar_eixoy(a,b,c):
    eixoy = []
    eixox = definir_eixox()
    for x in eixox:
        y = calcular_segundo_grau(a, b, c, x)
        eixoy.append(y)
    return eixoy

def pedir_valor(nomea):
    a = float(input(f"Informe o valor de {nomea}: "))
    return a

def calcular_delta(a,b,c):
    delta = (b**2) - 4*a*c
    return delta

def calcular_raizes(a, b, delta):
    if delta < 0:
        parte_real = -b / (2 * a)
        parte_imaginaria = (-delta)**0.5 / (2 * a)
        raiz1 = complex(parte_real, parte_imaginaria)
        raiz2 = complex(parte_real, -parte_imaginaria)
        return raiz1, raiz2
    elif delta == 0:
        raiz = -b / (2 * a)
        return raiz
    else:
        raiz1 = (-b + (delta**0.5)) / (2 * a)
        raiz2 = (-b - (delta**0.5)) / (2 * a)
        return raiz1, raiz2

def calcular_verticiex(b,a):
    vx=-b/(2*a)
    return vx

def calcular_verticiey(delta,a):
    vy=-delta/(4*a)
    return vy

def gerar_grafico(a,b,c):
    x = definir_eixox()
    y = gerar_eixoy(a, b, c)
    plt.plot(x, y)
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title('Gráfico de uma função de segundo grau')
    plt.grid(True)
    plt.show()

def escolha_2():
        print("Perfeito, opção (função de segundo grau) selecionada!")
        while True:
            a = pedir_valor("a")
            if a != 0:
                b = pedir_valor("b")
                c = pedir_valor("c")
                break
            else:
                print("Não é uma equação de segundo grau...\nInforme o valor de a diferente de zero!")
                continue
            
        while True:
            linha_menu()
            print("E - Calcular raízes")
            print("F - Calcular função em x pedido")
            print("G - Calcular Vértice ")
            print("H - Gerar gráfico")
            print("0 - Voltar")
            linha_menu()
            escolha_letra_2 = str(input("Digite a letra da opção desejada: "))
            if escolha_letra_2 == '0':
                print("Voltando ao menu principal.")
                break
            delta=calcular_delta(a,b,c)
            if escolha_letra_2 == 'e':
                    raizes=calcular_raizes(a,b,delta)
                    if delta < 0:
                        linha()
                        print(f"Existem duas raizes complexas {raizes}")
                        linha()
                        sleep()
                    elif delta == 0:
                        linha()
                        print(f"Existe uma raiz real {raizes}" )
                        linha()
                        sleep()
                    else:
                        linha()
                        print(f"Existem duas raizes reais {raizes}")
                        linha()
                        sleep()

            elif escolha_letra_2 == 'f':
                print("Ok, vamos calcular a função em X pedido:")
                x = pedir_valor('X')
                resultado = calcular_segundo_grau(a, b, c, x)
                linha()
                print(f"Para a função f(x) = {a}x² + {b}x + {c}, quando x = {x}, o resultado é: {resultado}")
                linha()
                sleep()

            elif escolha_letra_2 == 'g':
                print("Ok, vamos calcular o vértice:")
                x_vertice = calcular_verticiex(b,a)
                y_vertice = calcular_verticiey(delta,a)
                linha()
                print(f"O x do vértice da parábola é :{x_vertice}\nO y do vértice da parábola é :{y_vertice}")
                linha()
                sleep
                if a>0:
                    linha()
                    print('Ponto de Mínimo')
                    linha()
                    sleep()
                else:
                    linha()
                    print('Ponto de Máximo')
                    linha()
                    sleep()

            elif escolha_letra_2 == 'h': 

                gerar_grafico(a, b, c)
            else:
                print("Opção inválida. Tente novamente.")
                continue

def calcular_exponencial(a, b, x):
    y=a*b**x
    return y

def eixoy_exponencial(a,b,x):
    eixoy=[]
    eixox=definir_eixox()
    for x in eixox:
        y=calcular_exponencial(a,b,x)
        eixoy.append(y)
    return eixoy

def gerar_grafico_exponencial(a, b,x):
    x = definir_eixox()
    y = eixoy_exponencial(a, b, x)
    plt.plot(x, y)
    plt.title('Função Exponencial')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.grid(True)
    plt.show()
  
def escolha_3():
    linha()
    print("Perfeito, opção (funções exponenciais) selecionada!")
    linha()
    print('Informe os valores!')
    while True:
        valor_a = pedir_valor('a')
        if valor_a==0:
            print('A função resultará em zero!\nDigite um valor diferente de 0')
            continue
        else:
            valor_b = pedir_valor('b')
            if valor_b==1 or valor_b<=0:
                print("Caso de inexistência, digite um valor para b que seja maior que zero e diferente de 1 ")
                continue
            else:
                valor_x = float(input("Digite o valor de X para calcular a função: "))
                break
    
    while True:
        linha_menu()
        print("I - Verificar se é crescente ou decrescente")
        print("J - calcular função em x pedido")
        print("K - Gerar gráfico")
        print("0 - Voltar")
        linha_menu()
        escolha_letra_3 = input("Digite a letra da opção desejada: ").lower()
        linha()
        if escolha_letra_3 == '0':
            print("Voltando ao menu principal...")
            sleep()
            break
        if escolha_letra_3 == 'i':
                print("Ok, vamos verificar se a função é crescente ou decrescente")
                if valor_b > 1 and valor_a > 0:
                    linha()
                    print("A função é crescente!")
                    linha()
                    sleep()
                    
                elif 0 < valor_b < 1 and valor_a < 0:
                    linha()
                    print("A função é crescente!")
                    linha()
                    sleep()
                    
                else:
                    print("A função é decrescente")
                
        elif escolha_letra_3 == 'j':
            resultado = calcular_exponencial(valor_a, valor_b, valor_x)
            linha()
            print(f"Para a função f(x) = {valor_a} * {valor_b}^x, quando x = {valor_x}, o resultado é: {resultado}")
            linha()
            sleep()
            continue
        elif escolha_letra_3 == 'k': 
            gerar_grafico_exponencial(valor_a,valor_b,valor_x)
            continue              
        else:
            print("Opção inválida. Tente novamente.")
            continue

def imprimir_matrizes_multiplicacao(matriza,matrizb,matrizc):
    print('\n    Matriz A   X   B   +   AXB\n')
    for i in range(len(matriza)):
        linha=""
    # O número de linhas da matriz resultante será igual ao número de linhas da primeira matriz
        for elemento in matriza[i]:
            linha+=str(elemento) + " "
        linha+="   "
        for elemento in matrizb[i]:
            linha+=str(elemento) + " "
        linha+="   "  
        for elemento in matrizc[i]:
            linha+=str(elemento) + " "
        print(linha)
        #Foi como um acumulador e no fim printa a "linha" que acumulou

def escolha_4():
        linha()
        print("Perfeito, opção (matrizes) selecionada!")
        linha()
        linhasMA=pedir_informacao_matriz('linhas','A')
        colunasMA=pedir_informacao_matriz('colunas','A')
        matriz_A=gerar_matriz(linhasMA,colunasMA)
        imprimir_matriz(matriz_A)
        while True:
            linha_menu()
            print("O que voce deseja fazer?")
            print("L - Determinante (2X2 ou 3x3) - Verificar se é matriz quadrada ")
            print("M - Multiplicação ")
            print("N - Matriz transposta")
            print("0 - Voltar")
            linha_menu()
            escolhaLetra_4 = input("Digite a letra da opção desejada: ").lower()
            if escolhaLetra_4 == '0':
                print("Voltando ao menu principal...")
                sleep()
                break
            if escolhaLetra_4 == 'l':
                if verificar_matriz_quadrada(matriz_A):
                    linha()
                    print('Essa é uma matriz quadrada')
                    linha()
                    if verificar_matriz2x2(matriz_A):
                        linha()
                        print(f'O determinate dessa matriz 2x2 é: {calcular_determinate2x2 (matriz_A)}')
                        linha()
                        sleep()

                    if verificar_matriz3x3(matriz_A):
                        linha()
                        print(f'O determinante dessa matriz 3x3 é: {calcular_determinate3x3(matriz_A)}')
                        linha()
                        sleep()
                else:
                    linha()
                    print('Essa matriz NÃO é quadrada, portanto o número linha é diferente do número de colunas!')
                    linha()
                    sleep()
            elif escolhaLetra_4 == 'm':
                linhaMB=pedir_informacao_matriz('linhas','B')
                colunaMB=pedir_informacao_matriz('colunas','B')
                matriz_B=gerar_matriz(linhaMB,colunaMB)
                imprimir_matriz(matriz_B)
                if verificacao_multiplicacao(matriz_A,matriz_B):
                    print('É possível realizar essa multplicação de matrizes!')
                    matriz_C=multiplicar_matrizes(matriz_A,matriz_B)
                    linha()
                    imprimir_matrizes_multiplicacao(matriz_A,matriz_B,matriz_C)     
                    linha()
                    sleep()           
                else:
                    linha()
                    print('É impossivel multiplicar essas matrizes, pois o número de colunas da primeira matriz é diferente do número de linhas da segunda matriz!')  
                    linha()
                    sleep()
                    break  
            elif escolhaLetra_4 == 'n':
                transposta=calcula_matriz_trasposta(matriz_A)
                linha()
                print("Matriz transposta")
                imprimir_matriz(transposta)
                linha()
                sleep()
            else:
                print("Opção inválida. Digite novamente!")
                continue

def gerar_matriz(num_linhas,num_colunas):
    matriz=[]
    for i in range(num_linhas):
        linha=[]
        for j in range(num_colunas):
            elemento=float(input(f'Digite o valor do elemento {i+1},{j+1}: '))
            linha.append(elemento)
        matriz.append(linha)  
    return matriz      

def imprimir_matriz(matriz):
    for i in matriz:
        print(i)

def calcula_matriz_trasposta(matriz):
    nlinhas=len(matriz)
    ncolunas=len(matriz[0])
    transposta=[]
    for i in range(ncolunas):
        linha_transposta=[]
        for j in range(nlinhas):
            linha_transposta.append(matriz[j][i])
        transposta.append(linha_transposta)   
    return transposta     

def matriz_3x3(linha0,linha1,linha2):
    matriz = [linha0,linha1,linha2]
    print("Matriz 3x3")
    for linha in matriz:
        print(linha)
    return matriz 

def pedir_informacao_matriz(pedido,nome_matriz):
    resposta=int(input(f'Digite o número de {pedido} da sua matriz {nome_matriz}: '))
    return resposta

def verificacao_multiplicacao(matriza,matrizb):
    if len(matriza[0]) == len(matrizb):
        return True
    else:
        return False
        
def multiplicar_matrizes(matriza,matrizb):
    matrizc=[]
    nlinhas=len(matriza)
    ncolunas=len(matrizb[0])
    for i in range(nlinhas):
        linha_multiplicaacao=[]
        for j in range(ncolunas):
            elemento=0
            for k in range(len(matrizb)):
                #tanto faz usar o len(matrizb)=Número de linhas da matriz B ou usar o len(matriza[0])=Número de colunas da matriz A
                elemento+=matriza[i][k]*matrizb[k][j]
            linha_multiplicaacao.append(elemento)   
        matrizc.append(linha_multiplicaacao)   
    return matrizc  

def verificar_matriz_quadrada(matriz):
    nlinhas=len(matriz)
    ncolunas=len(matriz[0])
    if nlinhas == ncolunas:
        return True
    else:
        return False     
    
def verificar_matriz3x3(matriz):
    nlinhas=len(matriz)
    ncolunas=len(matriz[0])
    if nlinhas==3 and ncolunas==3:
        return True
    else:
        return False
    
def verificar_matriz2x2(matriz):
    nlinhas=len(matriz)
    ncolunas=len(matriz[0])
    if nlinhas==2 and ncolunas==2:
        return True
    else:
        return False    
    
def calcular_determinate2x2(matriz):    
    diagonal_principal=[]
    diagonal_principal.append(matriz[0][0])
    diagonal_principal.append(matriz[1][1])
    diagonal_secundaria=[]
    diagonal_secundaria.append(matriz[0][1])
    diagonal_secundaria.append(matriz[1][0])
    determinante=(diagonal_principal[0]*diagonal_principal[1])-(diagonal_secundaria[0]*diagonal_secundaria[1])
    return determinante

def calcular_determinate3x3(matriz):
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]
    
    det = (a * e * i) + (b * f * g) + (c * d * h) - (c * e * g) - (b * d * i) - (a * f * h)
    
    return det


####  programa principal ####

while True:
    try:
        menu()  
        opcao = escolha_opcao()
        if opcao == 0:
            break
        if opcao == 1:
            escolha_1()
        elif opcao == 2:
            escolha_2()
        elif opcao == 3:
            escolha_3()
        elif opcao == 4:
            escolha_4()
        else:
            print('Opção inválida, digite novamente!')
            continue
    except ValueError:
        print('Opção inválida, digite novamente!')