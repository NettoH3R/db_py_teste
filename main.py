from functions import *

try:

    while True:
        print("1. Inserir nova pessoa \n2. Consultar pessoas \n3. Sair")

        num = int(input("Entre com a opção desejada: "))
        print("\n")


        if num == 1:
            nome = str(input("Digite o nome da pessoa: "))
            idade = int(input("Digite a idade da pessoa: "))
            print("\n")
            
            if nome and idade:
                inserir_pessoa(nome,idade)
            else:
                print("Valor invalido digitado")
                break
        
        elif num == 2:
            consultar_pessoas()
        
        elif num == 3:
            print("Programa Encerrado \nByeee✌️")
            break

        else:
            print("Valor invalido")
    
except:
    print("Valor invalido")
