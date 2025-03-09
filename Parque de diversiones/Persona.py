class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
    def calcular_descuento(self):
        if self.edad<10:
            return 5*0.25
        
        else:
            return 5*0.0
        
    def nuevo_costo(self):
        return 5-self.calcular_descuento()