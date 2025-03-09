import tkinter as tk
from tkinter import messagebox

class Sumaapp:
    def __init__(self, root):
        self.root = root
        self.root.title("Suma al rededor de 100")
        
        self.numero_label=tk.Label(root,text="Número a sumar")
        self.numero_label.pack()
        self.numero_entry=tk.Entry(root)
        self.numero_entry.pack()
        
        self.Sumar_button=tk.Button(root,text="Sumar números",command=self.Sumar_numeros)
        self.Sumar_button.pack()
        
        self.suma = 0
        
        self.suma_label=tk.Label(root,text="La suma es: 0")
        self.suma_label.pack()
        
    def Sumar_numeros(self):
        try:
            numero=int(self.numero_entry.get())
            
            if self.suma <= 100:
                self.suma += numero
                self.numero_entry.delete(0, tk.END)
                self.numero_entry.focus()
                self.suma_label.config(text=f"La suma es: {self.suma}")
                
            else:
                messagebox.showinfo("Sumatoria", f"La sumatoria mayor a 100 de los numeros ingresados es: {self.suma}")
                self.root.quit()
            
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número entero positivo")