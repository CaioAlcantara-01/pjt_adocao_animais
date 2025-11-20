from sqlalchemy import Column, Integer, String
from .database import Base

class Animal(Base):
    __tablename__ = "animais"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    idade = Column(Integer)
    especie = Column(String)
    status = Column(String, default="disponível")

    __mapper_args__ = {
        "polymorphic_identity": "animal",
        "polymorphic_on": especie,
    }

    def emitir_som(self):
        pass

class Cachorro(Animal):
    __mapper_args__ = {
        "polymorphic_identity": "cachorro",
    }

    def emitir_som(self):
        return "Au au!"

class Gato(Animal):
    __mapper_args__ = {
        "polymorphic_identity": "gato",
    }

    def emitir_som(self):
        return "Miau!"