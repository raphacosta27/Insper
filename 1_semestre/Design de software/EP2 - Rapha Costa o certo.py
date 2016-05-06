def ler_escolha():
    while True:
        escolhas_possiveis = [0,1,2,3,4]
        print(">> Menu de escolhas: ")
        print("0 - sair")
        print("1 - adicionar item")
        print("2 - remover item")
        print("3 - alterar item")                               
        print("4 - imprimir relatorio")
        escolha = int(input("Faça sua escolha: "))
        if not escolha in escolhas_possiveis:
            print("O número deve estar entre 0 e 4")
        else:
            return escolha

def ler_nome():
    nome_do_produto = input("Digite o nome do produto: ")
    return nome_do_produto

def ler_valor():
    while True: 
        valor_do_produto = float(input("Digite o valor do produto: "))
        if valor_do_produto < 0:
            print ("Digite um valor positivo")
        else:
            return valor_do_produto

def achar_item(lista,nome):
    for i in range (len(lista)):
        if lista[i][0] == nome:
            return i
    return -1

def imprimir_itens(lista):
    for i in range(len(lista)):
        nome = lista[i][0]
        preço = lista[i][1]
        print ("{0}: {1}".format(nome,preço))

def computar_total(lista):
    valor_total = 0
    for i in range(len(lista)):
        preços = lista[i][1]
        valor_total += preços
    return valor_total 

def imprimir_relatorio(lista):
    imprimir_itens(lista)
    total = computar_total(lista)
    print("O valor total da compra é {0}".format(total))

lista_principal = []
while True:
    opcao_escolhida = ler_escolha()
    if opcao_escolhida == 0:
        print("Até Mais")
        break
    elif opcao_escolhida == 1:
        nome_adicionado = ler_nome()
        valor_adicionado = ler_valor()
        lista_principal.append([nome_adicionado, valor_adicionado])
        print()
    elif opcao_escolhida == 2:
        produto_a_ser_removido = ler_nome()
        achar_produto_a_ser_removido = achar_item(lista_principal,produto_a_ser_removido)
        while True:
            if achar_produto_a_ser_removido == -1:
                print("Elemento não encontrado")
                print()
                break
            else:
                del lista_principal[achar_produto_a_ser_removido]
                print()                
                break
    elif opcao_escolhida == 3:
        produto_a_ser_substituido = ler_nome()
        achar_produto_a_ser_substituido = achar_item(lista_principal, produto_a_ser_substituido)
        while True:
            if achar_produto_a_ser_substituido == -1:
                print("Elemento não encontrado")
                print()                
                break
            else:
                valor_para_substituir = ler_valor()
                lista_principal[achar_produto_a_ser_substituido] = [produto_a_ser_substituido, valor_para_substituir]
                break
                print()
    elif opcao_escolhida == 4:
        imprimir_relatorio(lista_principal)
    else:
        print("Opção Inválida")
        
    
    
    
        
        
        
        
        
        
        
        
        