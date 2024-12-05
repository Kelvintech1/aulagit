import tkinter as tk
from tkinter import ttk
from classes import Jogadores, Tecnicos  # Importar as classes
import shared_data  # Arquivo para compartilhar dados


class CadastroApp(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        # Campos para cadastro
        tk.Label(self, text="Nome:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entrada_nome = tk.Entry(self)
        self.entrada_nome.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text="Idade:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entrada_idade = tk.Entry(self)
        self.entrada_idade.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self, text="Posição (Jogador):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entrada_posicao = tk.Entry(self)
        self.entrada_posicao.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self, text="Experiência (Técnico):").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.entrada_experiencia = tk.Entry(self)
        self.entrada_experiencia.grid(row=3, column=1, padx=5, pady=5)

        # Botões para cadastro
        tk.Button(self, text="Cadastrar Jogador", command=self.cadastrar_jogador).grid(row=4, column=0, padx=5, pady=10)
        tk.Button(self, text="Cadastrar Técnico", command=self.cadastrar_tecnico).grid(row=4, column=1, padx=5, pady=10)

    def cadastrar_jogador(self):
        nome = self.entrada_nome.get()
        idade = self.entrada_idade.get()
        posicao = self.entrada_posicao.get()
        if nome and idade and posicao:
            jogador = Jogadores(nome, idade, posicao)
            shared_data.time_lista.append(jogador)
            self.limpar_campos()

    def cadastrar_tecnico(self):
        nome = self.entrada_nome.get()
        idade = self.entrada_idade.get()
        experiencia = self.entrada_experiencia.get()
        if nome and idade and experiencia:
            tecnico = Tecnicos(nome, idade, experiencia)
            shared_data.time_lista.append(tecnico)
            self.limpar_campos()

    def limpar_campos(self):
        self.entrada_nome.delete(0, tk.END)
        self.entrada_idade.delete(0, tk.END)
        self.entrada_posicao.delete(0, tk.END)
        self.entrada_experiencia.delete(0, tk.END)
