class Veiculo:
    #Atributos
    def __init__(self,peso,potencia,carga):
        self.peso = peso
        self.potencia = potencia
        self.carga = carga

    def relacao_peso_potencia(self):
        return self.peso/self.potencia
        
    def getPotenciaKW(self):
        potenciakw = self.potencia * 0.736
        return potenciakw
    
veiculo1 = Veiculo(170,900,4)
veiculo2 = Veiculo(97,1200,2.5)
veiculos = [veiculo1, veiculo2]

soma_dos_pesos = 0 
for cada in veiculos:
    soma_dos_pesos += cada.peso 

print(soma_dos_pesos)    