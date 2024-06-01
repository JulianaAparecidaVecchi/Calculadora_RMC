import numpy as np
import matplotlib.pyplot as plt

def calcular_segundo_grau(a, b, c, x):
    return a * x**2 + b * x + c

def definir_eixox():
    x = np.linspace(-10, 10, 1000)  # Reduzindo o intervalo para -10 a 10
    return x

def gerar_eixoy(a, b, c):
    eixoy = []
    eixox = definir_eixox()
    for x in eixox:
        y = calcular_segundo_grau(a, b, c, x)
        eixoy.append(y)
    return eixoy

def gerar_grafico(a, b, c):
    x = definir_eixox()
    y = gerar_eixoy(a, b, c)
    plt.plot(x, y)
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title('Gráfico de uma função de segundo grau')
    plt.grid(True)
    plt.show()

# Coeficientes da equação de segundo grau
a = 1
b = 0
c = 0

# Gerar o gráfico
gerar_grafico(a, b, c)
