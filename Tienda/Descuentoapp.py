import tkinter as tk
from tkinter import messagebox
from Compra import Compra

class Descuentoapp:
    
    def __init__(self, root):
        self.root=root
        self.root.title("Descuento de Octubre")
        
        self.mes_label=tk.Label(root,text="Mes")
        self.mes_label.pack()
        self.mes_entry=tk.Entry(root)
        self.mes_entry.pack()
        
        self.monto_label=tk.Label(root,text="Monto")
        self.monto_label.pack()
        self.monto_entry=tk.Entry(root)
        self.monto_entry.pack()
        
        self.Calcular_button=tk.Button(root,text="Calcular descuento",command=self.Calcular_descuento)
        self.Calcular_button.pack()
        
    def Calcular_descuento(self):
        mes=self.mes_entry.get()
        monto=float(self.monto_entry.get())
        compra=Compra(mes,monto)
        descuento=compra.calcular_descuento()
        nuevo_costo=compra.nuevo_costo()
        messagebox.showinfo("Descuento obtenido",f"Descuento:${descuento:.2f}\nMonto final:${nuevo_costo:.2f}")
        
if __name__=="__main__":
    root=tk.Tk()
    Descuentoapp = Descuentoapp(root)
    root.mainloop()