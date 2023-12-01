import tkinter
import tkinter as tk
from datetime import datetime
from tkinter import ttk
from tkinter import messagebox
# if condicional
# def funcion

#  ================== $$$ Ventana $$$ ==================
main_window = tk.Tk()
etiqueta = tk.Label(main_window, text="Ingrese el nombre de la tarea:")
main_window.title("lista de tareas")
treeview = ttk.Treeview(columns=("size", "lastmod")) #columnas size tamaño de cada archivo lastmod fecha
treeview.heading("#0", text="Descripcion")
treeview.heading("size", text="Fecha")
treeview.heading("lastmod", text="Completado")
etiqueta.pack()

texto = tk.Entry(main_window)
texto.pack()
# ================== $$$ Agrega tarea $$$ ================== 
def agregar():
        today = datetime.today()
        fecha = f"{today.day}/{today.month}/{today.year}"
        treeview.insert("", tk.END, text= texto.get(), values=(fecha, False))
        texto.delete(0, tk.END)
    
# ================== $$$ marcar como completada $$$ ==================
def marcar_completada():
    selected_item = treeview.selection()
    if selected_item:
        treeview.item(selected_item, values=(treeview.item(selected_item)['values'][0], True))
    else:
        messagebox.showinfo("Error", "Selecciona una tarea antes de marcar como completada")

# ================== $$$ Borrar tarea $$$ ==================
def borrar():
    selected_item = treeview.selection()  #si no hay lista con elementos devuelve vacio
    if selected_item:
        treeview.delete(selected_item)  

# ================== $$$ Salir $$$ ==================
def salir():
    # Agregar confirmación antes de salir
    resultado = messagebox.askokcancel("Confirmar", "¿Estás seguro de que quieres salir?")
    if resultado:
        main_window.quit()
# ================== $$$ Botones $$$ ==================
btn_guardar = tkinter.Button(main_window, bg= "green", text="Agregar", command = agregar)
btn_borrar = tkinter.Button(main_window, bg=  "red", text="Borrar", command = borrar)
salir_btn = tkinter.Button(main_window, bg=  "blue", text="exit", command = salir)
btn_marcar_completada = tkinter.Button(main_window, bg="yellow", text="Marcar como Completada", command=marcar_completada)
btn_guardar.pack()
btn_guardar.pack()
btn_borrar.pack()
salir_btn.pack() 
btn_marcar_completada.pack()

# ================== $$$ Botones Horizontales Frame $$$ ==================
button_frame = tk.Frame(main_window)     #almacena los botones
button_frame.pack()                      #permite ajustar el tamaño
                                         
btn_guardar.pack(side=tk.LEFT)           #lado izquierdo 
btn_borrar.pack(side=tk.LEFT)
salir_btn.pack(side=tk.LEFT)
btn_marcar_completada.pack(side=tk.LEFT)

treeview.pack()

main_window.mainloop() 