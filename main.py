import tkinter as tk
from tkinter import ttk
from cadastro import CadastroApp
from lista import ListaApp


# Janela principal
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cadastro de Time")
        self.geometry("400x400")
        self.create_tabs()

    def create_tabs(self):
        abas = ttk.Notebook(self)
        aba_cadastro = CadastroApp(abas)
        aba_lista = ListaApp(abas)
        abas.add(aba_cadastro, text="Cadastro")
        abas.add(aba_lista, text="Lista de Time")
        abas.pack(expand=1, fill="both")


# Executar o aplicativo
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
