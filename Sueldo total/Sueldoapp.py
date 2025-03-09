import tkinter as tk
from tkinter import messagebox
from Empleado import Empleado

class Sueldoapp:
    
    def __init__(self, root):
        self.root=root
        self.root.title("Calculadora de Sueldo Final")
        
        self.nombre_label=tk.Label(root,text="Nombre")
        self.nombre_label.pack()
        self.nombre_entry=tk.Entry(root)
        self.nombre_entry.pack()
        
        self.horas_normales_label=tk.Label(root,text="Horas normales trabajadas")
        self.horas_normales_label.pack()
        self.horas_normales_entry=tk.Entry(root)
        self.horas_normales_entry.pack()
        
        self.horas_extras_label=tk.Label(root,text="Horas extras trabajadas")
        self.horas_extras_label.pack()
        self.horas_extras_entry=tk.Entry(root)
        self.horas_extras_entry.pack()
        
        self.hijos_label=tk.Label(root,text="Hijos")
        self.hijos_label.pack()
        self.hijos_entry=tk.Entry(root)
        self.hijos_entry.pack()
        
        self.Calcular_button=tk.Button(root,text="Calcular sueldo",command=self.Calcular_sueldo)
        self.Calcular_button.pack()
        
    def Calcular_sueldo(self):
        nombre=self.nombre_entry.get()
        horas_normales=float(self.horas_normales_entry.get())*100
        horas_extras=float(self.horas_extras_entry.get())*150
        hijos=int(self.hijos_entry.get())
        
        empleado=Empleado(nombre,horas_normales,horas_extras,hijos)
        sueldo_final=empleado.sueldo_final()
        
        horas_normales_formateado = "{:.2f}".format(horas_normales)
        horas_extras_formateado = "{:.2f}".format(horas_extras)
        bono_formateado = "{:.2f}".format(empleado.calcular_bono())
        sueldo_final_formateado = "{:.2f}".format(sueldo_final)
        
        messagebox.showinfo("Sueldo final",
                            f"Nombre: {nombre}\n"
                            f"Sueldo de horas normales: ${horas_normales_formateado}\n"
                            f"Sueldo de horas extras: ${horas_extras_formateado}\n"
                            f"Bonificación por hijos: ${bono_formateado}\n"
                            f"Sueldo final: ${sueldo_final_formateado}\n"
                            f"El sueldo por hora normal trabajada es de $100\n"
                            f"La hora extra es pagada 50% más que la normal")
        
if __name__=="__main__":
    root=tk.Tk()
    Sueldoapp = Sueldoapp(root)
    root.mainloop()