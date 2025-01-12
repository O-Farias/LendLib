from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
import datetime

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    
    emprestimos = relationship('Emprestimo', back_populates='usuario')

class Livro(Base):
    __tablename__ = 'livros'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    disponivel = Column(Integer, default=1)  

    
    emprestimos = relationship('Emprestimo', back_populates='livro')

class Emprestimo(Base):
    __tablename__ = 'emprestimos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    livro_id = Column(Integer, ForeignKey('livros.id'), nullable=False)
    data_emprestimo = Column(DateTime, default=datetime.datetime.utcnow)
    data_devolucao = Column(DateTime, nullable=True)

    
    usuario = relationship('Usuario', back_populates='emprestimos')
    livro = relationship('Livro', back_populates='emprestimos')
