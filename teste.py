def calcular_matriz_adicionada(matriz):
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    matriz_adicionada = []
    for i in range(nlinhas):
        linha = []
        for j in range(ncolunas):
            linha.append(matriz[i][j])
        for k in range(2):  # Adiciona os dois primeiros elementos ao final da linha
            linha.append(matriz[i][k])
        matriz_adicionada.append(linha)
    return matriz_adicionada

    
def definir_eixox():
    np.arege()

def imprimir_matriz(matriz):
    for i in matriz:
        print(i)

matriz=[[3,2,3],[3,2,5],[4,5,6]]  
re=calcular_matriz_adicionada(matriz)   
print(re)  
prin