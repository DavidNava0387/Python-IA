import tkinter as tk
from tkinter import messagebox

class Sumaapp:
    def __init__(self, root):
        self.root = root
        self.root.title("Suma de enteros")
        
        self.numero_label=tk.Label(root,text="Número hasta cual sumar")
        self.numero_label.pack()
        self.numero_entry=tk.Entry(root)
        self.numero_entry.pack()
        
        self.Sumar_button=tk.Button(root,text="Sumar números",command=self.Sumar_numeros)
        self.Sumar_button.pack()
        
        self.suma = 0
        
    def Sumar_numeros(self):
        try:
            numero=int(self.numero_entry.get())
            
            if numero <= 0:
                messagebox.showerror("Error", f"Debes ingresar un número positivo")
                return
                
            else:
                self.suma = (numero * (numero + 1)) / 2
                messagebox.showinfo("Sumatoria", f"La suma de los primeros {numero} enteros es: {self.suma}")
            
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número entero positivo")