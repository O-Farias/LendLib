from app.services import criar_usuario, adicionar_livro, registrar_emprestimo, listar_emprestimos

def menu():
    while True:
        print("\n=== LendLib ===")
        print("1. Criar Usuário")
        print("2. Adicionar Livro")
        print("3. Registrar Empréstimo")
        print("4. Listar Empréstimos")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o email do usuário: ")
            usuario = criar_usuario(nome, email)
            print(f"Usuário criado: {usuario.nome} ({usuario.email})")
        elif opcao == "2":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            livro = adicionar_livro(titulo, autor)
            print(f"Livro adicionado: {livro.titulo} por {livro.autor}")
        elif opcao == "3":
            usuario_id = int(input("Digite o ID do usuário: "))
            livro_id = int(input("Digite o ID do livro: "))
            try:
                emprestimo = registrar_emprestimo(usuario_id, livro_id)
                print(f"Empréstimo registrado para o livro ID {livro_id}.")
            except Exception as e:
                print(f"Erro: {e}")
        elif opcao == "4":
            emprestimos = listar_emprestimos()
            for emp in emprestimos:
                print(f"[ID {emp.id}] Usuário ID {emp.usuario_id} - Livro ID {emp.livro_id} - Data {emp.data_emprestimo}")
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()
