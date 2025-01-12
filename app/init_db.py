from app.database import Base, get_engine
from app.models import Usuario, Livro, Emprestimo

def criar_tabelas():
    engine = get_engine()
    print("Criando tabelas no banco de dados...")
    Base.metadata.create_all(engine)
    print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    criar_tabelas()
