class Barata:
    
    def __init__ (self,ligado,saudacao,potencia):
        self.ligado = ligado
        self.saudacao = saudacao
        self.potencia = potencia
    
    def diz_oi(self):
        self.saudacao = print("oi")
 
    def liga(self):
        self.ligado = True
    
    def desliga(self):
        self.ligado = False
    
    def muda_potencia(self, nova_potencia):
        if nova_potencia > 0:
            self.potencia = nova_potencia
        else:
            self.potencia = 0
            
        

barata1 = Barata(True, "bom dia amiguinho", 10000)
barata2 = Barata(True, "bom dia é o....", 30)

barata1.diz_oi()
barata2.diz_oi()

