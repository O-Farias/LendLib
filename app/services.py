from app.models import Usuario, Livro, Emprestimo
from app.database import get_session

def criar_usuario(nome, email):
    session = get_session()
    usuario = Usuario(nome=nome, email=email)
    session.add(usuario)
    session.commit()
    return usuario

def adicionar_livro(titulo, autor):
    session = get_session()
    livro = Livro(titulo=titulo, autor=autor)
    session.add(livro)
    session.commit()
    return livro

def registrar_emprestimo(usuario_id, livro_id):
    session = get_session()
    livro = session.query(Livro).filter_by(id=livro_id, disponivel=1).first()

    if not livro:
        raise Exception("Livro não disponível para empréstimo.")

    emprestimo = Emprestimo(usuario_id=usuario_id, livro_id=livro_id)
    livro.disponivel = 0  # Marca o livro como emprestado
    session.add(emprestimo)
    session.commit()
    return emprestimo

def listar_emprestimos():
    session = get_session()
    return session.query(Emprestimo).all()
