from app.services import criar_usuario, adicionar_livro, registrar_emprestimo, listar_emprestimos, buscar_livros_google

def menu():
    while True:
        print("\n=== LendLib ===")
        print("1. Criar Usuário")
        print("2. Adicionar Livro")
        print("3. Registrar Empréstimo")
        print("4. Listar Empréstimos")
        print("5. Buscar Livros (Google Books)")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Criação de usuário
            nome = input("Digite o nome do usuário: ").strip()
            email = input("Digite o email do usuário: ").strip()
            if nome and email:
                try:
                    usuario = criar_usuario(nome, email)
                    print(f"✅ Usuário criado com sucesso: {usuario.nome} ({usuario.email})")
                except Exception as e:
                    print(f"⚠️ Erro: {e}")
            else:
                print("⚠️ Nome ou email inválido. Tente novamente.")
        
        elif opcao == "2":
            # Adicionar livro
            titulo = input("Digite o título do livro: ").strip()
            autor = input("Digite o autor do livro: ").strip()
            if titulo and autor:
                try:
                    livro = adicionar_livro(titulo, autor)
                    print(f"✅ Livro adicionado com sucesso: '{livro.titulo}' por {livro.autor}")
                except Exception as e:
                    print(f"⚠️ Erro: {e}")
            else:
                print("⚠️ Título ou autor inválido. Tente novamente.")
        
        elif opcao == "3":
            # Registrar empréstimo
            try:
                usuario_id = int(input("Digite o ID do usuário: "))
                livro_id = int(input("Digite o ID do livro: "))
                emprestimo = registrar_emprestimo(usuario_id, livro_id)
                print(f"✅ Empréstimo registrado com sucesso para o livro ID {livro_id}.")
            except ValueError:
                print("⚠️ IDs de usuário ou livro devem ser números. Tente novamente.")
            except Exception as e:
                print(f"⚠️ Erro: {e}")
        
        elif opcao == "4":
            # Listar empréstimos
            emprestimos = listar_emprestimos()
            if not emprestimos:
                print("⚠️ Nenhum empréstimo registrado até o momento.")
            else:
                print("\n📚 Empréstimos Registrados:")
                for emp in emprestimos:
                    print(f"[ID {emp.id}] Usuário: {emp.usuario.nome} - Livro: {emp.livro.titulo} - Data: {emp.data_emprestimo}")
        
        elif opcao == "5":
            # Buscar livros na Google Books API
            query = input("Digite o título ou autor para buscar: ").strip()
            if query:
                try:
                    resultados = buscar_livros_google(query)
                    if resultados:
                        print("\n📚 Resultados da Busca:")
                        for idx, livro in enumerate(resultados, 1):
                            print(f"{idx}. {livro['titulo']} - Autor(es): {livro['autores']}")
                            print(f"   Descrição: {livro['descricao']}")
                            if livro['imagem']:
                                print(f"   Imagem: {livro['imagem']}")
                            print("\n")
                    else:
                        print("⚠️ Nenhum livro encontrado para a pesquisa.")
                except Exception as e:
                    print(f"⚠️ Erro: {e}")
            else:
                print("⚠️ Termo de busca inválido. Tente novamente.")
        
        elif opcao == "6":
            # Sair do menu
            print("Saindo... 👋")
            break
        
        else:
            print("⚠️ Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()
