# LendLib - Sistema de Empréstimos de Livros

LendLib é um sistema simples de gerenciamento de empréstimos de livros, criado com **Python** e **SQLAlchemy**, com suporte à integração com a **Google Books API** para busca de livros. Este projeto foi desenvolvido para fins educacionais, com foco na organização de código backend e boas práticas de desenvolvimento.

## 🎯 Funcionalidades

- **Gerenciamento de usuários**
  - Criar usuários.
  - Listar usuários cadastrados.

- **Gerenciamento de livros**
  - Adicionar livros ao sistema.
  - Buscar livros na **Google Books API**.

- **Gerenciamento de empréstimos**
  - Registrar empréstimos de livros.
  - Listar empréstimos registrados.

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **SQLAlchemy**: ORM para manipulação do banco de dados SQLite.
- **Google Books API**: Integração para busca de livros online.
- **Colorama**: Para estilização do terminal.

## 📂 Estrutura de Diretórios

```plaintext
LendLib/
├── app/
│   ├── __init__.py
│   ├── cli.py          # Interface de linha de comando (menu principal)
│   ├── database.py     # Configuração do banco de dados
│   ├── init_db.py      # Script de inicialização do banco de dados
│   ├── models.py       # Definição das tabelas do banco
│   ├── services.py     # Lógica de negócio
├── migrations/         # Pasta para futuras migrações de banco de dados
├── tests/              # Testes unitários
│   ├── __init__.py
│   ├── test_services.py
├── venv/               # Ambiente virtual (adicionado ao .gitignore)
├── .env                # Variáveis de ambiente (adicionado ao .gitignore)
├── lendlib.db          # Banco de dados SQLite (adicionado ao .gitignore)
├── requirements.txt    # Dependências do projeto
├── README.md           # Documentação do projeto
```

## 🚀 Como Rodar o Projeto

### Pré-requisitos

- **Python 3.10+** instalado.
- Gerenciador de pacotes `pip` configurado.

### Passo a Passo

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/O-Farias/lendlib.git
   cd lendlib
   ```

2. **Crie um ambiente virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**:
   Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
   ```plaintext
   DATABASE_URL=sqlite:///lendlib.db
   GOOGLE_BOOKS_API_KEY=sua_chave_da_google_books_api
   ```

5. **Inicialize o banco de dados**:
   ```bash
   PYTHONPATH=. python app/init_db.py
   ```

6. **Execute a aplicação**:
   ```bash
   PYTHONPATH=. python app/cli.py
   ```

## 🧪 Testes

Para rodar os testes unitários, execute:
```bash
PYTHONPATH=. pytest tests/
```

## 🔑 Chave da API do Google Books

- Para usar a funcionalidade de busca de livros, você precisa de uma chave de API da **Google Books**.
- Acesse o [Google Cloud Console](https://console.cloud.google.com/) para gerar sua chave de API.

## 📚 Funcionalidades da Interface

1. **Criar Usuário**: Adicione um novo usuário ao sistema.
2. **Adicionar Livro**: Insira um novo livro manualmente.
3. **Registrar Empréstimo**: Registre um empréstimo associando um livro a um usuário.
4. **Listar Empréstimos**: Veja todos os empréstimos registrados no sistema.
5. **Buscar Livros (Google Books)**: Pesquise livros online usando a Google Books API.
6. **Sair**: Encerre o programa.

## 🛡️ Boas Práticas

- **Segurança**: Nunca compartilhe suas credenciais ou o arquivo `.env`.
- **Colaboração**: Use o `.gitignore` para evitar adicionar arquivos sensíveis ao repositório.
- **Modularidade**: O código foi organizado em módulos para facilitar manutenção e expansão.

## 💡 Melhorias Futuras

- Implementação de autenticação para usuários.
- Geração de relatórios de empréstimos.
- Interface gráfica (GUI) ou aplicação web.

## 🖼️ Exemplo do Menu no Terminal

```plaintext
=== LendLib - Sistema de Empréstimos de Livros ===
==================================================
[1] Criar Usuário
[2] Adicionar Livro
[3] Registrar Empréstimo
[4] Listar Empréstimos
[5] Buscar Livros (Google Books)
[6] Sair
==================================================
Escolha uma opção:
```

## 👨‍💻 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

Feito com ❤️ por [Mateus Farias](https://github.com/O-Farias).
