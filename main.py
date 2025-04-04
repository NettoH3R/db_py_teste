from functions import *

try:

    while True:
        print("1. Inserir nova pessoa \n2. Consultar pessoas \n3. Sair")

        num = int(input("Ente com a opção desejada: "))


        if num == 1:
            nome = str(input("Digite o nome da pessoa: "))
            idade = int(input("Digite a idade da pessoa: "))
            
            if nome and idade:
                inserir_pessoa(nome,idade)
            else:
                print("Valor invalido digitado")
                break
        
        elif num == 2:
            consultar_pessoas()
        
        elif num == 3:
            break
    
except:
    print("Valor invalido")
