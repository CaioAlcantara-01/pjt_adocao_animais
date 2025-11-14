from fastapi import FastAPI
from app.models import Animal, Cachorro, Gato

app = FastAPI()


animais = []

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo à adoção de animais!"}



@app.post("/animais/")
def adicionar_animal(tipo: str, nome: str, idade: int):
    if tipo.lower() == "cachorro":
        novo = Cachorro(nome, idade, "Cachorro")
    elif tipo.lower() == "gato":
        novo = Gato(nome, idade, "Gato")
    else:
        return {"erro": "Tipo de animal inválido."}
    
    animais.append(novo)
    return {"mensagem": f"{novo.nome} cadastrado com sucesso!", "som": novo.emitir_som()}



@app.get("/animais/")
def listar_animais():
    lista = []
    for a in animais:
        lista.append({
            "nome": a.nome,
            "idade": a.idade,
            "espécie": a.especie,
            "status": a.status
        })
    return lista



@app.put("/animais/adotar/{nome}")
def adotar_animal(nome: str):
    for a in animais:
        if a.nome.lower() == nome.lower():
            if a.status == "adotado":
                return {"mensagem": f"{a.nome} já foi adotado."}
            a.status = "adotado"
            return {"mensagem": f"{a.nome} foi adotado com sucesso!"}
    return {"erro": "Animal não encontrado."}



@app.delete("/animais/{nome}")
def remover_animal(nome: str):
    for a in animais:
        if a.nome.lower() == nome.lower():
            animais.remove(a)
            return {"mensagem": f"{a.nome} removido da lista."}
    return {"erro": "Animal não encontrado."}



@app.get("/animais/especie/{tipo}")
def listar_por_especie(tipo: str):
    lista = [a.nome for a in animais if a.especie.lower() == tipo.lower()]
    return {"espécie": tipo, "animais": lista}