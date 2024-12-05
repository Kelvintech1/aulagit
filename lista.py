import tkinter as tk
from tkinter import ttk
import shared_data  # Importar a lista compartilhada


class ListaApp(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        self.lista_texto = tk.Text(self, wrap=tk.WORD, width=50, height=20)
        self.lista_texto.pack(padx=10, pady=10)
        self.atualizar_lista()

    def atualizar_lista(self):
        self.lista_texto.delete(1.0, tk.END)
        for item in shared_data.time_lista:
            self.lista_texto.insert(tk.END, str(item) + "\n")
