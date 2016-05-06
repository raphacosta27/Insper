# -*- coding: utf-8 -*-
"""
Solução exercício 1, aula 11, versão condensada
"""

def converte_data(data_americana):
    data = data_americana.split()
    mda = data[0].split("/")
    hm = data[1].split(":")
    if data[2] == "PM":
        hm[0] = str(int(hm[0]) + 12)
    return "{0}/{1}/{2} {3}:{4}".format(mda[1], mda[0], mda[2], hm[0], hm[1])
    
# Codigo de teste
print(converte_data("02/29/2016 5:32 PM"))
