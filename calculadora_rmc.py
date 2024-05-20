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

def verificar_subconjunto(a,b):
    return a<b

def pedir_primeiro_conjunto(lista):
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
            pedir_primeiro_conjunto(conjunto_a)
            print('Informe o conjunto B')
            pedir_primeiro_conjunto(conjunto_b)
            if opcao_conjunto==1:
                if verificar_subconjunto(conjunto_a,conjunto_b):
                    envelopar(print(f'{conjunto_a} é subconjunto próprio de {conjunto_b}'))
                else:
                    envelopar(print(f'{conjunto_a} NÃO é subconjunto próprio de {conjunto_b}'))     
                
            elif opcao_conjunto==2:
                pass
            elif opcao_conjunto==3:
                pass
            elif opcao_conjunto==4:
                pass
            elif opcao_conjunto > 4 or opcao_conjunto<0 :
                linha()
                print('Erro!\nDigite uma opção válida!')
                linha()
                pausa(1)
                continue                

            
    elif opcao==2:
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