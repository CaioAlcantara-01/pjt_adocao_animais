from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Animal, Cachorro, Gato
from app.database import Base, engine, get_db

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo à adoção de animais!"}

@app.post("/criar/animais/")
def adicionar_animal(tipo: str, nome: str, idade: int, db: Session = Depends(get_db)):
    if tipo.lower() == "cachorro":
        novo = Cachorro(nome=nome, idade=idade)
    elif tipo.lower() == "gato":
        novo = Gato(nome=nome, idade=idade)
    else:
        return {"erro": "Tipo de animal inválido."}
    
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return {"mensagem": f"{novo.nome} cadastrado com sucesso!", "som": novo.emitir_som()
}

@app.get("/listar/animais/")
def listar_animais(db: Session = Depends(get_db)):
    animais = db.query(Animal).all()
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
def adotar_animal(nome: str, db: Session = Depends(get_db)):
    animal = db.query(Animal).filter(Animal.nome == nome).first()
    if not animal:
        return {"erro": "Animal não encontrado."}
    
    if animal.status == "adotado":
        return {"mensagem": f"{animal.nome} já foi adotado."}
    
    animal.status = "adotado"
    db.commit()
    return {"mensagem": f"{animal.nome} foi adotado com sucesso!"}

@app.delete("/animais/{nome}")
def remover_animal(nome: str, db: Session = Depends(get_db)):
    animal = db.query(Animal).filter(Animal.nome == nome).first()
    if not animal:
        return {"erro": "Animal não encontrado."}
    
    db.delete(animal)
    db.commit()
    return {"mensagem": f"{animal.nome} removido da lista."}

@app.get("/animais/especie/{tipo}")
def listar_por_especie(tipo: str, db: Session = Depends(get_db)):
    animais = db.query(Animal).filter(Animal.especie == tipo.lower()).all()
    lista = [a.nome for a in animais]
    return {"espécie": tipo, "animais": lista}