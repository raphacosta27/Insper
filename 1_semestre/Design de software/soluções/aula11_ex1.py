# -*- coding: utf-8 -*-
"""
Solução exercício 1, aula 11
"""

def converte_data(data_americana):
    # Passo 1: separa data, horario e AM/PM usando split().
    lista_data_horario_ampm = data_americana.split()
    data = lista_data_horario_ampm[0]
    horario = lista_data_horario_ampm[1]
    am_pm = lista_data_horario_ampm[2]
    
    # Passo 2: separa mes, dia e ano usando split("/").
    lista_mes_dia_ano = data.split("/")
    mes = lista_mes_dia_ano[0]
    dia = lista_mes_dia_ano[1]
    ano = lista_mes_dia_ano[2]

    # Passo 3: separa hora e minuto usando split(":").
    lista_hora_minuto = horario.split(":")
    hora = lista_hora_minuto[0]
    minuto = lista_hora_minuto[1]    
    
    # Passo 3: corrige a hora se horário for PM.
    if am_pm == "PM":
        hora_int = int(hora)
        hora_int += 12
        hora = str(hora_int)
    
    # Passo 4: monta a data brasileira.
    data_brasileira = "{0}/{1}/{2} {3}:{4}".format(dia, mes, ano, hora, minuto)
    
    return data_brasileira
    
# Codigo de teste
print(converte_data("02/29/2016 5:32 PM"))
