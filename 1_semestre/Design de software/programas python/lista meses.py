mes = int(input("Qual o número do mês? "))
lista_mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio","Junho","Julho","Agosto", "Setembro","Outubro","Novembro","Dezembro"]
print(lista_mes[(mes - 1) % 12])
