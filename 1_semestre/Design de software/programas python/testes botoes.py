def conta_palavras(lista_de_palavras):
    contagem = {}
    for palavra in lista_de_palavras:
        if palavra in contagem:
            contagem[palavra] += 1 
        else:
            contagem[palavra] = 1
    return contagem         
palavras = ['happy', 'birthday', 'to', 'you',
            'happy', 'birthday', 'to', 'you',
            'happy', 'birthday',
            'happy', 'birthday',
            'happy', 'birthday', 'to', 'you']
contagem_de_palavras = conta_palavras(palavras)
print(contagem_de_palavras)