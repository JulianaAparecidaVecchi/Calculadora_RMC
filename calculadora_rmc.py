import time
def envelopar(msg):
    print(60*'-')
    msg
    print(60*'-')

def pausa(x):
    time.sleep(x)

def menu_principal():
    print('Essas são suas opções:\n        |MENU|\n[1]-Conjuntos númericos\n[2]-Funções do Segundo Grau\n[3]-Fuções Exponenciais\n[4]-Matrizes\n[0]-Sair')
    escolha=int(input("Oque deseja calcular?\n"))
    return escolha

def menu_conjuntos():
    print('Essas são suas opções:\n        |MENU|\n[1]-Verificar se A é subconjunto próprio de B\n[2]-(Realizar operação de União\n[3]-(Calcular intersecção\n[4]-Calcular diferença\n[0]-Voltar')
    escolha=int(input("Oque deseja fazer?\n"))
    return escolha

def menu_grau2():
    print('Essas são suas opções:\n        |MENU|\n[1]-Calcular Raízes\n[2]-Calcular função em x\n[3]-Calcular o vértice\n[4]-Gerar gráfico\n[0]-Voltar')
    escolha=int(input("Oque deseja fazer?\n"))
    return escolha

def verificar_subconjunto(a,b):
    return a<b

def realizar_uniao(a,b):
    return a|b

def pedir_conjunto(lista):
    e = 1
    while True:
        resposta = input(f'Digite o {e}º elemento do seu conjunto (ou "Parar" para terminar): ')
        e += 1
        if resposta == "Parar" or resposta=="parar":
            break
        else:
            if isinstance(resposta, str): 
                lista.append(resposta)  
            elif isinstance(resposta,int):
                lista.append(int(resposta))  
            elif isinstance(resposta,float):
                lista.append(float(resposta))  

    return lista  

def pedir_numero(letra):
    numero=float(input(f'Digite um para {letra} número:'))
    return numero

conjunto_a=[]   
conjunto_b=[] 






while True:
    print('***********|   CALCULADORA RMC   |***********')
    opcao=menu_principal()
    if opcao==0:
        print('Encerrando...')
        pausa(1)
        break       
    if opcao==1:
        while True:
            opcao_conjunto=menu_conjuntos()
            if opcao_conjunto==0:
                print('Voltando...')
                pausa(1)
                break
                print('Informe o conjunto A')
                pedir_conjunto(conjunto_a)
                print('Informe o conjunto B')
                pedir_conjunto(conjunto_b)
                if opcao_conjunto==1:
                    if verificar_subconjunto(conjunto_a,conjunto_b):
                        envelopar(print(f'{conjunto_a} é subconjunto próprio de {conjunto_b}'))
                    else:
                        envelopar(print(f'{conjunto_a} NÃO é subconjunto próprio de {conjunto_b}'))         
                elif opcao_conjunto==2:
                    teste=realizar_uniao(A,B)
                elif opcao_conjunto==3:
                    pass
                elif opcao_conjunto==4:
                    pass
            elif opcao_conjunto > 4 or opcao_conjunto<0 :   
                envelopar(print('Erro!\nDigite uma opção válida!'))
                pausa(1)
                continue                         
    elif opcao==2:
        while True:
            opcao_grau2=menu_grau2()
            if opcao_grau2==0:
                print('Voltando...')
                pausa(1)
                break
            if opcao_grau2 < 0 or opcao_grau2 > 4:
                envelopar(print('Erro!\nDigite uma opção válida!'))
                pausa(1)
                continue 
            while True:
                a_grau2=pedir_numero('a')
                b_grau2=pedir_numero('b')
                c_grau2=pedir_numero('c')
                if a_grau2==0:
                    print('Para ser possível calcula informe "a" diferente de zero!\nInforme os valores novamente!')
                    continue
                else:
                    if opcao_grau2==1:
                        print(a_grau2+b_grau2)
                        break
                    elif opcao_grau2==2:
                        pass
                    elif opcao_grau2==3:   
                        pass 
                    elif opcao_grau2==4:
                        pass                 
    elif opcao==3:
        pass
    elif opcao==4:
        pass
    elif opcao > 4 or opcao < 0:
        linha()
        print('Erro!\nDigite uma opção válida!')
        linha()
        pausa(1)
        continue