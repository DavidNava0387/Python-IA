class Compra:
    def __init__(self,mes,monto):
        self.mes=mes
        self.monto=monto
        
    def calcular_descuento(self):
        if self.mes.lower()=="octubre":
            descuento = self.monto * 0.15
        
        else:
            descuento = 0
        return descuento
        
    def nuevo_costo(self):
        descuento = self.calcular_descuento()
        return self.monto - descuento