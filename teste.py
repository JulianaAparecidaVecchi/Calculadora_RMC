def gerar_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            elemento = float(input(f'Digite o valor do elemento {i+1},{j+1}: '))
            linha.append(elemento)
        matriz.append(linha)  
    return matriz      

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)


def calcula_matriz_transposta(matriz):
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    transposta = []
    for i in range(ncolunas):
        linha_transposta = []
        for j in range(nlinhas):
            linha_transposta.append(matriz[j][i])
        transposta.append(linha_transposta)
    return transposta        

matriz = gerar_matriz(6, 6)
print("Matriz:")
imprimir_matriz(matriz)

transposta = calcula_matriz_transposta(matriz)
print("\nTransposta da Matriz:")
imprimir_matriz(transposta)
