def frase(nome, curso = "Design de Software", escola = "Insper"):
    print("{0} é aluno de {1} no {2}".format(nome, curso, escola))
frase ("Voce")   
frase ("Voce", "ModSim")
frase ("Voce", escola = "UniDuniTe")
