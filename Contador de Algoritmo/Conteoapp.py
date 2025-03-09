import tkinter as tk
from tkinter import messagebox

class Conteoapp:
    def __init__(self, root):
        self.root = root
        self.root.title("¿De 0 a 20?")
        
        self.numero_label=tk.Label(root,text="Número")
        self.numero_label.pack()
        self.numero_entry=tk.Entry(root)
        self.numero_entry.pack()
        
        self.Comprobar_button=tk.Button(root,text="Comprobar número",command=self.Comprobar_numero)
        self.Comprobar_button.pack()
        
        self.contador = 0
        
        self.contador_label=tk.Label(root,text="Intentos: 0")
        self.contador_label.pack()
        
    def Comprobar_numero(self):
        try:
            self.contador += 1
            
            numero=float(self.numero_entry.get())
            
            if numero > 0 and numero < 20:
                self.contador_label.config(text=f"Intentos: {self.contador}")
                messagebox.showinfo("Número dentro del rango", f"El número ingresado es: {numero}")
                self.contador=0
                
            else:
                self.numero_entry.delete(0, tk.END)
                self.numero_entry.focus()
                self.contador_label.config(text=f"Intentos: {self.contador}")
            
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número entero")