from sqlalchemy import \
    Column, Integer, String, ForeignKey

from database import Base


class Estudante(Base):
    __tablename__ = 'estudantes'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    idade = Column(Integer)
    email = Column(String, unique=True, index=True)


class Matricula(Base):
    __tablename__ = 'matriculas'

    id = Column(Integer,
                primary_key=True,
                index=True)

    estudante_id = Column(
        Integer,
        ForeignKey('estudantes.id'),
        nullable=False
    )

    curso_nome = Column(
        String,
        index=True
    )

    ano = Column(Integer)
