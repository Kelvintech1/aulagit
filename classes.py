from abc import ABC, abstractmethod


# Classe abstrata Time
class Time(ABC):
    @abstractmethod
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


# Classe concreta Jogadores
class Jogadores(Time):
    def __init__(self, nome, idade, posicao):
        super().__init__(nome, idade)
        self.posicao = posicao

    def __str__(self):
        return f"Jogador: {self.nome}, Idade: {self.idade}, Posição: {self.posicao}"


# Classe concreta Técnicos
class Tecnicos(Time):
    def __init__(self, nome, idade, experiencia):
        super().__init__(nome, idade)
        self.experiencia = experiencia

    def __str__(self):
        return f"Técnico: {self.nome}, Idade: {self.idade}, Experiência: {self.experiencia} anos"

