import tkinter as tk
from tkinter import messagebox

class Validacionapp:
    def __init__(self, root):
        self.root = root
        self.root.title("¿De 0 a 20?")
        
        self.numero_label=tk.Label(root,text="Número")
        self.numero_label.pack()
        self.numero_entry=tk.Entry(root)
        self.numero_entry.pack()
        
        self.Comprobar_button=tk.Button(root,text="Comprobar número",command=self.Comprobar_numero)
        self.Comprobar_button.pack()
        
    def Comprobar_numero(self):
        try:
            numero=float(self.numero_entry.get())
            
            if numero > 0 and numero < 20:
                messagebox.showinfo("Número dentro del rango", f"El número ingresado es: {numero}")
                
            else:
                self.numero_entry.delete(0, tk.END)
                self.numero_entry.focus()
            
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número entero")