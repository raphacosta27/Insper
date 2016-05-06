def contador_de_palavras(lista):
    contador = {}
    for palavra in lista:
        if palavra in contador:
            contador[palavra] += 1
        else:
            contador[palavra] = 1
    return contador        
lista_de_palavras = ["happy","birthday","to","you","happy","birthday","happy","birthday","happy","birthday","to","you"]            
teste = contador_de_palavras(lista_de_palavras)
print(teste)