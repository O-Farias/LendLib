from app.models import Usuario, Livro, Emprestimo
from app.database import get_session


def criar_usuario(nome, email):
    """Cria um novo usuário no sistema."""
    session = get_session()

    # Verifica se o e-mail já está cadastrado
    usuario_existente = session.query(Usuario).filter_by(email=email).first()
    if usuario_existente:
        raise Exception(f"Usuário com e-mail {email} já está cadastrado.")

    usuario = Usuario(nome=nome, email=email)
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario


def adicionar_livro(titulo, autor):
    """Adiciona um novo livro ao sistema."""
    session = get_session()

    # Verifica se o livro já está cadastrado
    livro_existente = session.query(Livro).filter_by(titulo=titulo, autor=autor).first()
    if livro_existente:
        raise Exception(f"O livro '{titulo}' de {autor} já está cadastrado.")

    livro = Livro(titulo=titulo, autor=autor)
    session.add(livro)
    session.commit()
    session.refresh(livro)
    return livro


def registrar_emprestimo(usuario_id, livro_id):
    """Registra o empréstimo de um livro."""
    session = get_session()

    # Verifica se o livro está disponível
    livro = session.query(Livro).filter_by(id=livro_id, disponivel=1).first()
    if not livro:
        raise Exception("Livro não disponível para empréstimo.")

    # Verifica se o usuário existe
    usuario = session.query(Usuario).filter_by(id=usuario_id).first()
    if not usuario:
        raise Exception(f"Usuário com ID {usuario_id} não encontrado.")

    emprestimo = Emprestimo(usuario_id=usuario_id, livro_id=livro_id)
    livro.disponivel = 0  # Marca o livro como emprestado
    session.add(emprestimo)
    session.commit()
    session.refresh(emprestimo)
    return emprestimo


def listar_emprestimos():
    """Lista todos os empréstimos registrados."""
    session = get_session()
    emprestimos = session.query(Emprestimo).all()

    # Retorna uma lista vazia se não houver empréstimos
    return emprestimos

