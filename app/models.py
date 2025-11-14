from abc import ABC, abstractmethod


class Animal(ABC):
    def _init_(self, nome: str, idade: int, especie: str, status: str = "disponível"):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.status = status

    @abstractmethod
    def emitir_som(self):
        pass

 
 
class Cachorro(Animal):
    def emitir_som(self):
        return "Au au!"


class Gato(Animal):
    def emitir_som(self):
        return "Miau!"