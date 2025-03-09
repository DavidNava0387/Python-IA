class Empleado:
    def __init__(self,nombre,horas_normales,horas_extras,hijos):
        self.nombre=nombre
        self.horas_normales=horas_normales
        self.horas_extras=horas_extras
        self.hijos=hijos
        
    def calcular_bono(self):
        return self.hijos*0.05 * (self.horas_extras + self.horas_normales)
        
    def calcular_sueldo_final(self):
        return self.horas_extras + self.horas_normales + self.calcular_bono()
        
    def sueldo_final(self):
        return self.calcular_sueldo_final()