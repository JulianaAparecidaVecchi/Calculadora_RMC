import time
import numpy as np
import matplotlib

def linha():
    print(80*"-")

def sleep():
    time.sleep(1)

def menu():
    linha()
    print("Calculadora - Escolha sua operação aritmética!")
    linha()
    sleep()
    print("1 - Conjuntos numéricos")
    sleep()
    print("2 - Funções de segundo grau")
    sleep()
    print("3 - Funções exponenciais")
    sleep()
    print("4 - Matrizes")
    sleep()
    print("5 - Sair da calculadora")
    sleep()



def escolha_opcao(): 
    linha()
    escolha = int(input("Digete o número da opção desejada!\n"))
    linha()
    if escolha == 1:
        print("Perfeito, opção (conjuntos numérios) selecionada!")
        linha()
        print("O que voce deseja fazer?")
        print("A - Verificar se A é subconjunto próprio de B")
        print("B - Realizar operação de União")
        print("C - Calcular intersecção")
        print("D - Calcular diferença")
        print("0 - Voltar")
    elif escolha == 2:
        print("Perfeito, opção (função de segundo grau) selecionada!")
        linha()
        print("O que voce deseja fazer?")
        print("E - Calcular raízes")
        print("F - Calcular função em x pedido")
        print("G - Calcular Vértice ")
        print("H - Gerar gráfico")
        print("0 - Voltar")
    elif escolha == 3:
        print("Perfeito, opção (funções exponenciais) selecionada!")
        linha()
        print("O que voce deseja fazer?")
        print("I - Verificar se é crescente ou decrescente")
        print("J - calcular função em x pedido")
        print("K - Gerar gráfico")
        print("0 - Voltar")
    elif escolha == 4:
        print("Perfeito, opção (matrizes) selecionada!")
        linha()
        print("O que voce deseja fazer?")
        print("L - Determinante (2X2 ou 3x3) - Verificar se é matriz quadrada ")
        print("M - Multiplicação ")
        print("N - Matriz transposta")
        print("0 - Voltar")
    if escolha == 5:
        print("Tchau! Até uma próxima...")
        linha()
        return escolha
    return escolha       
    
def escolha_1():
    global menu, escolha_opcao
    linha()
    escolhaLetra1 = str(input("Digite a letra da opção desejada!\n"))
    linha()
    if escolhaLetra1 == 0:
        print("Voltando...")
    else:
        print("Agora coloque seus conjuntos!")
        conj1 = set(input("Digite o conjunto A!\n "))
        conj2 = set(input("Digite o conjunto B!\n "))
        if escolhaLetra1.lower() == 'a':
            if conj1 <= conj2 and conj1 != conj2:
                print("A é um subconjunto próprio de B")
            elif conj2 <= conj1 and conj2 != conj1:
                print("A não é um subconjunto próprio de B, mas B é um subconjunto próprio de A")
            else:
                print("A não é um subconjunto próprio de B")   
        
        elif escolhaLetra1.lower() == 'b':
            uniao = conj1|conj2
            print(f" A união é: {uniao}")        
        
        elif escolhaLetra1.lower() == 'C':
            interseccao = conj1 & conj2
            print(f" A intersecção é: {interseccao}")
        
        elif escolhaLetra1.lower() == 'D':
            diferenca = conj1 - conj2
            print(f"A diferença é: {diferenca}")

        else:
            print("Opção inválida. Tente novamente.")

def calcular_segundo_grau(a, b, c, x):
    return a * x ** 2 + b * x + c

def escolha_2():
    while True:
        linha()
        escolha_letra_2 = input("Digite a letra da opção desejada: ").lower()
        linha()
        if escolha_letra_2 == 'e':
            a = float(input("Digite o valor de a: "))
            print("Ok, vamos calcular as raízes!")
            if a != 0:
                b = float(input("Informe o valor de b: "))
                c = float(input("Informe o valor de c: "))
                delta = (b**2) - 4*a*c
                if delta < 0:
                    print("O valor de delta é igual a %.1f e não possui raízes reais" % delta)
                elif delta == 0:
                    raiz = (-b + delta**0.5)/(2*a)
                    print("O valor de delta é igual a %.1f e possui apenas uma raiz igual a %.1f" % (delta, raiz))
                else:
                    raiz1 = (-b + delta**0.5)/(2*a)
                    raiz2 = (-b - delta**0.5)/(2*a)
                    print("O valor de delta é igual a %.1f" % delta)
                    print("Valor da raiz 1 = %.1f" % raiz1)
                    print("Valor da raiz 2 = %.1f" % raiz2)
            else:
                print("Não é uma equação de segundo grau...")

        elif escolha_letra_2 == 'f':
            print("Ok, vamos calcular a função em X pedido:")
            a = float(input("Digite o valor de a: "))
            x = float(input("Digite o valor de x: "))
            b = float(input("Informe o valor de b: "))
            c = float(input("Informe o valor de c: "))
            resultado = calcular_segundo_grau(a, b, c, x)
            print(f"Para a função f(x) = {a}x^2 + {b}x + {c}, quando x = {x}, o resultado é: {resultado}")

        elif escolha_letra_2 == 'g':
            print("Ok, vamos calcular o vértice:")
            a = float(input("Digite o valor de a: "))
            if a != 0:
                b = float(input("Informe o valor de b: "))
                c = float(input("Informe o valor de c: "))
                delta = (b ** 2) - 4 * a * c
                if delta >= 0:
                    x_vertice = -b / (2 * a)
                    y_vertice = -delta / (4 * a)
                    print(f"O vértice da parábola é ({x_vertice}, {y_vertice})")
                else:
                    print("A parábola não possui vértice real.")
            else:
                print("Não é uma equação de segundo grau...")

        elif escolha_letra_2 == 'h': #####
            print("Ok, vamos gerar o gráfico:")

        elif escolha_letra_2 == '0':
            print("Voltando ao menu principal.")
            break

        else:
            print("Opção inválida. Tente novamente.")


def calcular_exponencial(a, b, x):
    return a * (b ** x)


def escolha_3():
    while True:
        linha()
        escolha_letra_3 = input("Digite a letra da opção desejada: ").lower()
        linha()
        if escolha_letra_3 == 'i':
            valor_a = float(input("Digite o valor de A: "))
            if valor_a < 0 or valor_a == 1:
                print("Valor de A incorreto! Tente novamente")
            else:
                print("Ok, vamos verificar se a função é crescente ou decrescente")
                if valor_a > 1:
                    print("A função é crescente!")
                elif valor_a > 0 and valor_a < 1:
                    print("A função é decrescente")
                else:
                    print("A função não é nem crescente nem decrescente.")
        
        elif escolha_letra_3 == 'j':
            valor_a = float(input("Digite o valor de A: "))
            valor_b = int(input("Digite o valor de B: "))
            valor_x = float(input("Digite o valor de X para calcular a função: "))
            resultado = calcular_exponencial(valor_a, valor_b, valor_x)
            print(f"Para a função f(x) = {valor_a} * {valor_b}^x, quando x = {valor_x}, o resultado é: {resultado}")
        
        elif escolha_letra_3 == 'k': #####
            print("Ok, vamos gerar o gráfico")       
        elif escolha_letra_3 == '0':
            print("Voltando ao menu principal.")
            break       
        else:
            print("Opção inválida. Tente novamente.")


def matriz_3x3(linha0,linha1,linha2):
    matriz = [linha0,linha1,linha2]
    print("Matriz 3x3")
    for linha in matriz:
        print(linha)
    return matriz 


def escolha_4():
    while True:
        linha()
        escolhaLetra_4 = input("Digite a letra da opção desejada: ").lower()
        linha()
        linhas=int(input('Digite o número de linhas da sua matriz: '))
        colunas=int(input('Digite o númeor de colunas da sua matriz: '))
        matriz_A=gerar_matriz(linhas,colunas)
        imprimir_matriz(matriz_A)
        if escolhaLetra_4 == 'l':
            print("Determinante (2X2 ou 3x3) - Verificar se é matriz quadrada")
        elif escolhaLetra_4 == 'm':
            print("Multiplicação")
        elif escolhaLetra_4 == 'n':
            transposta=calcula_matriz_trasposta(matriz_A)
            linha()
            print("Matriz transposta")
            imprimir_matriz(transposta)
            linha()
            

        elif escolhaLetra_4 == '0':
            print("Voltando ao menu principal.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            print("")

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



####  programa principal ####

while True:
    menu()  
    opcao = escolha_opcao()
    if opcao == 5:
        break
    elif opcao == 1:
        escolha_1()
    elif opcao == 2:
        escolha_2()
    elif opcao == 3:
        escolha_3()
    elif opcao == 4:
        escolha_4()