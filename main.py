from fastapi import FastAPI

app = FastAPI()

animais = {
    1: {"animal 1": "cachorro", "preço": 500},
    2: {"animal 2": "gato", "preço": 300},
    3: {"animal 3": "peixe", "preço": 10},
    4: {"animal 4": "arara", "preço": 450},

}


@app.get("/")
def home():
    return " Bem vindo à adoção de animais "


@app.get("/animais/{id_animais}")
def pegar_animal(id_animais: int):