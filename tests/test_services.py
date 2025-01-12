import pytest
from app.services import criar_usuario, adicionar_livro, registrar_emprestimo, listar_emprestimos
from app.database import get_session
from app.models import Base, Usuario, Livro, Emprestimo


@pytest.fixture(scope="function")
def setup_db():
    """Configura um banco de dados temporário para os testes."""
    session = get_session()
    Base.metadata.create_all(session.get_bind())  # Cria tabelas no banco
    yield session
    Base.metadata.drop_all(session.get_bind())  # Limpa tabelas após os testes


def test_criar_usuario(setup_db):
    """Testa a criação de um novo usuário."""
    usuario = criar_usuario("Teste Usuário", "teste@usuario.com")
    assert usuario.nome == "Teste Usuário"
    assert usuario.email == "teste@usuario.com"


def test_adicionar_livro(setup_db):
    """Testa a adição de um novo livro."""
    livro = adicionar_livro("Teste Livro", "Autor Teste")
    assert livro.titulo == "Teste Livro"
    assert livro.autor == "Autor Teste"


def test_registrar_emprestimo(setup_db):
    """Testa o registro de um empréstimo."""
    usuario = criar_usuario("Teste Usuário", "teste@usuario.com")
    livro = adicionar_livro("Teste Livro", "Autor Teste")

    emprestimo = registrar_emprestimo(usuario.id, livro.id)
    assert emprestimo.usuario_id == usuario.id
    assert emprestimo.livro_id == livro.id
    assert not livro.disponivel  # Verifica que o livro foi marcado como não disponível


def test_listar_emprestimos(setup_db):
    """Testa a listagem de empréstimos."""
    usuario = criar_usuario("Teste Usuário", "teste@usuario.com")
    livro = adicionar_livro("Teste Livro", "Autor Teste")
    registrar_emprestimo(usuario.id, livro.id)

    emprestimos = listar_emprestimos()
    assert len(emprestimos) == 1
    assert emprestimos[0].usuario_id == usuario.id
    assert emprestimos[0].livro_id == livro.id
