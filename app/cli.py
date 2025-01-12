from app.services import criar_usuario, adicionar_livro, registrar_emprestimo, listar_emprestimos, buscar_livros_google, listar_usuarios
from colorama import Fore, Style

def menu():
    while True:
        print(Fore.CYAN + "\n=== LendLib - Sistema de Empréstimos de Livros ===" + Style.RESET_ALL)
        print(Fore.YELLOW + "=" * 50 + Style.RESET_ALL)
        print(Fore.GREEN + "[1]" + Style.RESET_ALL + " Criar Usuário")
        print(Fore.GREEN + "[2]" + Style.RESET_ALL + " Adicionar Livro")
        print(Fore.GREEN + "[3]" + Style.RESET_ALL + " Registrar Empréstimo")
        print(Fore.GREEN + "[4]" + Style.RESET_ALL + " Listar Empréstimos")
        print(Fore.GREEN + "[5]" + Style.RESET_ALL + " Buscar Livros (Google Books)")
        print(Fore.GREEN + "[6]" + Style.RESET_ALL + " Listar Usuários")
        print(Fore.RED + "[7] Sair" + Style.RESET_ALL)
        print(Fore.YELLOW + "=" * 50 + Style.RESET_ALL)
        opcao = input(Fore.CYAN + "Escolha uma opção: " + Style.RESET_ALL)

        if opcao == "1":
            nome = input(Fore.CYAN + "Digite o nome do usuário: " + Style.RESET_ALL).strip()
            email = input(Fore.CYAN + "Digite o email do usuário: " + Style.RESET_ALL).strip()
            if nome and email:
                try:
                    usuario = criar_usuario(nome, email)
                    print(Fore.GREEN + f"✅ Usuário criado: {usuario.nome} ({usuario.email})" + Style.RESET_ALL)
                except Exception as e:
                    print(Fore.RED + f"⚠️ Erro: {e}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "⚠️ Nome ou email inválido. Tente novamente." + Style.RESET_ALL)

        elif opcao == "2":
            titulo = input(Fore.CYAN + "Digite o título do livro: " + Style.RESET_ALL).strip()
            autor = input(Fore.CYAN + "Digite o autor do livro: " + Style.RESET_ALL).strip()
            if titulo and autor:
                try:
                    livro = adicionar_livro(titulo, autor)
                    print(Fore.GREEN + f"✅ Livro adicionado: '{livro.titulo}' por {livro.autor}" + Style.RESET_ALL)
                except Exception as e:
                    print(Fore.RED + f"⚠️ Erro: {e}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "⚠️ Título ou autor inválido. Tente novamente." + Style.RESET_ALL)

        elif opcao == "3":
            try:
                usuario_id = int(input(Fore.CYAN + "Digite o ID do usuário: " + Style.RESET_ALL))
                livro_id = int(input(Fore.CYAN + "Digite o ID do livro: " + Style.RESET_ALL))
                emprestimo = registrar_emprestimo(usuario_id, livro_id)
                print(Fore.GREEN + f"✅ Empréstimo registrado para o livro ID {livro_id}." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "⚠️ IDs devem ser números. Tente novamente." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"⚠️ Erro: {e}" + Style.RESET_ALL)

        elif opcao == "4":
            emprestimos = listar_emprestimos()
            if not emprestimos:
                print(Fore.YELLOW + "⚠️ Nenhum empréstimo registrado." + Style.RESET_ALL)
            else:
                print(Fore.CYAN + "\n📚 Empréstimos Registrados:" + Style.RESET_ALL)
                for emp in emprestimos:
                    print(Fore.YELLOW + f"[ID {emp.id}] Usuário: {emp.usuario.nome} - Livro: {emp.livro.titulo}" +
                          f" - Data: {emp.data_emprestimo}" + Style.RESET_ALL)

        elif opcao == "5":
            query = input(Fore.CYAN + "Digite o título ou autor para buscar: " + Style.RESET_ALL).strip()
            if query:
                try:
                    resultados = buscar_livros_google(query)
                    print(Fore.CYAN + "\n📚 Resultados da Busca:" + Style.RESET_ALL)
                    for idx, livro in enumerate(resultados, start=1):
                        print(Fore.YELLOW + f"{idx}. {livro['titulo']} - Autor(es): {livro['autores']}" + Style.RESET_ALL)
                        print(f"   Descrição: {livro['descricao']}")
                        print(f"   Imagem: {livro['imagem']}\n")
                except Exception as e:
                    print(Fore.RED + f"⚠️ Erro: {e}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "⚠️ Pesquisa vazia. Tente novamente." + Style.RESET_ALL)

        elif opcao == "6":
            usuarios = listar_usuarios()
            if not usuarios:
                print(Fore.YELLOW + "⚠️ Nenhum usuário cadastrado." + Style.RESET_ALL)
            else:
                print(Fore.CYAN + "\n👤 Usuários Cadastrados:" + Style.RESET_ALL)
                for usuario in usuarios:
                    print(Fore.YELLOW + f"[ID {usuario.id}] Nome: {usuario.nome} - Email: {usuario.email}" + Style.RESET_ALL)

        elif opcao == "7":
            print(Fore.GREEN + "Saindo... 👋" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "⚠️ Opção inválida. Tente novamente." + Style.RESET_ALL)

if __name__ == '__main__':
    menu()
