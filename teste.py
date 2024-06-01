matriza = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matrizb = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
matrizc = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]

def imprimir_matrizes_multiplicacao(matriza,matrizb,matrizc):

    print('Matriz A   X   B   +   AXB\n')
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
imprimir_matrizes_multiplicacao(matriza,matrizb,matrizc)
