#F3nix
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
import os


def select_files():
    files = filedialog.askopenfilenames(filetypes=[("Archivos PDF", "*.pdf")])
    file_list.delete(0, tk.END)
    for file in files:
        file_list.insert(tk.END, file)


def merge_pdfs():
    merger = PdfMerger()
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")])
    
    if output_path:
        for item in file_list.get(0, tk.END):
            merger.append(item)
        
        with open(output_path, "wb") as output_file:
            merger.write(output_file)
        
        messagebox.showinfo("Éxito", "Los archivos PDF se fusionaron correctamente!")
        file_list.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No se ha seleccionado ningún archivo de salida!")


# Crear la ventana principal
root = tk.Tk()
root.title("PDF Fusión")
root.geometry("400x300")

# Crear el widget de la lista para mostrar los archivos seleccionados
file_list = tk.Listbox(root, selectmode=tk.MULTIPLE)
file_list.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Crear el botón para seleccionar archivos
select_button = tk.Button(root, text="Seleccionar PDFs", command=select_files, relief=tk.RAISED, bd=4)
select_button.pack(fill=tk.X, padx=10, pady=5)

# Crear el botón para combinar los PDFs seleccionados
merge_button = tk.Button(root, text="Unir PDFs", command=merge_pdfs, relief=tk.RAISED, bd=4)
merge_button.pack(fill=tk.X, padx=10, pady=5)

# Ejecutar la aplicación
root.mainloop()
