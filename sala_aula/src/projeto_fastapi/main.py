from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import SessionLocal, engine

# criar as tabelas no pgsql caso nao existam
models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# criar as rotas:
@app.post("/estudantes/",
          response_model=schemas.EstudanteResponse)
def criar_estudante(
        estudante: schemas.EstudanteCreate,
        db: Session = Depends(get_db)):

    db_estudante = models.Estudante(nome=estudante.nome,
                                    idade=estudante.idade,
                                    email=estudante.email)
    db.add(db_estudante)
    db.commit()
    db.refresh(db_estudante)
    return db_estudante


@app.get("/estudantes/",
         response_model=List[schemas.EstudanteResponse])
def ler_estudantes(skip: int = 0,
                   limit: int = 10,
                   db: Session = Depends(get_db)):
    estudantes = db.query(models.Estudante).offset(skip).limit(limit).all()
    return estudantes


@app.post("/matriculas/",
          response_model=schemas.MatriculaResponse)
def criar_matricula(
        matricula: schemas.MatriculaCreate,
        db: Session = Depends(get_db)):
    db_matricula = models.Matricula(estudante_id=matricula.estudante_id,
                                    curso_nome=matricula.curso_nome,
                                    ano=matricula.ano)
    db.add(db_matricula)
    db.commit()
    db.refresh(db_matricula)
    return db_matricula


@app.get("/matriculas/",
         response_model=List[schemas.MatriculaResponse])
def ler_matriculas(skip: int = 0,
                   limit: int = 10,
                   db: Session = Depends(get_db)):
    matriculas = db.query(models.Matricula).offset(skip).limit(limit).all()
    return matriculas
