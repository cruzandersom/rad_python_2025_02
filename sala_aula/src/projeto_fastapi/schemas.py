from pydantic import BaseModel

class EstudanteBase(BaseModel):

    nome: str
    idade: int
    email: str

class EstudanteCreate(EstudanteBase):
    pass


class EstudanteResponse(EstudanteBase):
    id: int

    class Config:
        from_atributes = True


class MatriculaBase(BaseModel):
    estudante_id: int
    curso_nome: str
    ano: int

class MatriculaCreate(MatriculaBase):
    pass

class MatriculaResponse(MatriculaBase):
    id: int

    class Config:
        from_atributes = True