import tkinter as tk
from tkinter import messagebox
from Persona import Persona

class Descuentoapp:
    
    def __init__(self, root):
        self.root=root
        self.root.title("Descuento en Parque de Diversiones")
        
        self.nombre_label=tk.Label(root,text="Nombre")
        self.nombre_label.pack()
        self.nombre_entry=tk.Entry(root)
        self.nombre_entry.pack()
        
        self.edad_label=tk.Label(root,text="Edad")
        self.edad_label.pack()
        self.edad_entry=tk.Entry(root)
        self.edad_entry.pack()
        
        self.Calcular_button=tk.Button(root,text="Calcular descuento",command=self.Calcular_descuento)
        self.Calcular_button.pack()
        
    def Calcular_descuento(self):
        nombre=self.nombre_entry.get()
        edad=int(self.edad_entry.get())
        persona=Persona(nombre,edad)
        descuento=persona.calcular_descuento()
        nuevo_costo=persona.nuevo_costo()
        messagebox.showinfo("Descuento obtenido",f"Descuento:${descuento:.2f}\nCosto final:${nuevo_costo:.2f} soles")
        
if __name__=="__main__":
    root=tk.Tk()
    Descuentoapp = Descuentoapp(root)
    root.mainloop()