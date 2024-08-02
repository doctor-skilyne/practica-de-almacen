import tkinter as tk
from tkinter import messagebox


def calcular_promedio():
    
    nombre = nombre_entry.get()
    nota1 = float(nota1_entry.get())
    nota2 = float(nota2_entry.get())
    nota3 = float(nota3_entry.get())
    nota4 = float(nota4_entry.get())
    
    promedio = (nota1 + nota2 + nota3 + nota4) / 4
    
   
    promedio_label.config(text=f"Promedio: {promedio:.2f}")
    
    guardar_datos(nombre, nota1, nota2, nota3, nota4, promedio)
    
    messagebox.showinfo("Éxito", "Datos guardados correctamente.")

def guardar_datos(nombre, nota1, nota2, nota3, nota4, promedio):
    with open('alumnos.txt', 'a') as archivo:
        archivo.write(f"{nombre}, {nota1}, {nota2}, {nota3}, {nota4}, {promedio:.2f}\n")

root = tk.Tk()
root.title("Registro de Notas")

root.configure(bg="#F7753B")

nombre_label = tk.Label(root, text="Nombre del alumno:",bg="#F7753B",fg="grey")
nombre_label.grid(row=0, column=0, padx=10, pady=10)
nombre_entry = tk.Entry(root)
nombre_entry.grid(row=0, column=1, padx=10, pady=10)

nota1_label = tk.Label(root, text="calificacion1:")
nota1_label.grid(row=1, column=0, padx=10, pady=10)
nota1_entry = tk.Entry(root)
nota1_entry.grid(row=1, column=1, padx=10, pady=10)

nota2_label = tk.Label(root, text="calificacion2:")
nota2_label.grid(row=2, column=0, padx=10, pady=10)
nota2_entry = tk.Entry(root)
nota2_entry.grid(row=2, column=1, padx=10, pady=10)

nota3_label = tk.Label(root, text="PRACTICA:")
nota3_label.grid(row=3, column=0, padx=10, pady=10)
nota3_entry = tk.Entry(root)
nota3_entry.grid(row=3, column=1, padx=10, pady=10)

nota4_label = tk.Label(root, text="EF:")
nota4_label.grid(row=4, column=0, padx=10, pady=10)
nota4_entry = tk.Entry(root)
nota4_entry.grid(row=4, column=1, padx=10, pady=10)

promedio_label = tk.Label(root, text="Promedio: --")
promedio_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

calcular_button = tk.Button(root, text="Calcular Promedio y Guardar", command=calcular_promedio)
calcular_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="WE")

root.mainloop()
