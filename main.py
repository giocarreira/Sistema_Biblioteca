from time import sleep
import json

class Livro:
    def __init__(self, autor, titulo, ano, avaliacao=None):
        self.autor = autor
        self.titulo = titulo
        self.ano = ano
        self.avaliacao = avaliacao

    def MostrarInfo(self):
        print(f"\n| Título - {self.titulo}")
        print(f"| Autor - {self.autor}")
        print(f"| Ano de lançamento - {self.ano}")
        if self.avaliacao != None:
            print(f"| Avaliação - {self.avaliacao} estrelas\n")
        else:
            print("| Livro ainda não avaliado!\n")

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.tipo = None
        self.biblioteca = []
        self.carregar_dados()

    def carregar_dados(self):
        try:
            with open("dados.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                self.usuarios = dados.get("usuarios", [])
                self.livros = [Livro(**livro) for livro in dados.get("livros", [])]
        except FileNotFoundError:
            self.salvar_dados()

    def salvar_dados(self):
        with open("dados.json", "w", encoding="utf-8") as arquivo:
            dados = {
                "usuarios": self.usuarios,
                "livros": [livro.__dict__ for livro in self.livros]
            }
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    def TelaInicio(self):
        self.tipo = int(input("Você está entrando como:\n1 - Usuário | 2 - Funcionário \n"))
        if self.tipo == 1:            
            self.ExibirMenu_Usuario()
        elif self.tipo == 2:
            login = input("Insira seu login de administrador:\n").title()
            senha = int(input("Insira sua senha:\n"))
            if login != 'Admin' or senha != 1234:
                print("Informações incorretas!\n")
                self.TelaInicio()
            else:
                print("Login efetuado com sucesso!\n")
                sleep(2)
                self.ExibirMenu_Funcionario()
        else:
            print("Erro! Você deve selecionar uma opção válida!")

    def ExibirMenu_Funcionario(self):
        while True:
            print("\n | MENU |\n")  
            print("1 - Cadastrar livro")
            print("2 - Exibir livros cadastrados")
            print("3 - Remover livro")
            print("4 - Buscar livro por título")
            print("5 - Sair")
            try:
                opcao = int(input("\nSelecione uma opção: \n"))
            except ValueError:
                print("Selecione uma opção válida.")
                while opcao < 1 or opcao > 5:
                    opcao = int(input("Erro! Selecione uma opção de 1 - 5."))
            if opcao == 1:
                self.CadastrarLivros()
            elif opcao == 2:        
                self.MostrarLivros()
            elif opcao == 3:
                self.RemoverLivro()
            elif opcao == 4:
                self.BuscarLivro()
            elif opcao == 5:
                print("Saindo...\n")
                sleep(2)
                self.TelaInicio()
            else: 
                print("Erro! Opção inválida!")

    def ExibirMenu_Usuario(self):
        while True:
            print("\n | MENU |\n")  
            print("1 - Minha biblioteca")
            print("2 - Buscar livros")
            print("3 - Avaliar livros")
            print("4 - Sair")
            print("5 - Efetuar o login")
            try:
                opcao = int(input("\nSelecione uma opção: \n"))
            except ValueError:
                print("Selecione uma opção válida.")
                while opcao < 1 or opcao > 5:
                    opcao = int(input("Erro! Selecione uma opção de 1 - 5."))
            if opcao == 1:
                self.ExibirMinhaBiblioteca_Usuario()
            elif opcao == 2:        
                self.BuscarLivros_Usuario()
            elif opcao == 3:
                self.AvaliarLivro()       
            elif opcao == 4:
                print("Saindo...\n")
                sleep(2)
                self.TelaInicio()   
            elif opcao == 5:
                opcao_login = int(input("1 - Possuo cadastro | 2 - Quero me cadastrar \n"))

                if opcao_login == 1:
                    login = input("Digite seu login: \n")
                    senha = input("Digite sua senha: \n")
                    encontrado = False

                    for usuario in self.usuarios:
                            if usuario['Nome'] == login and usuario['Senha'] == senha:
                                print(f"\nOlá, {login}! Bem-vindo(a) de volta!\n")
                                encontrado = True 
                    if not encontrado:
                        print("Login não encontrado!\n")

                elif opcao_login == 2:
                    login = input("Digite seu login: \n")
                    senha = input("Digite sua senha: \n")
                    
                    login_existente = any(usuario['Nome'] == login for usuario in self.usuarios)
                    while login_existente:
                        login = input("\nEsse login já está sendo utilizado! Digite novamente: \n")
                        login_existente = any(usuario['Nome'] == login for usuario in self.usuarios)

                    self.usuarios.append({'Nome': login, "Senha": senha})
                    self.salvar_dados()
                    print(f"\nUsuário cadastrado!\nSeja bem-vindo(a), {login}!\n")
                else:
                    print("Opção inválida! Voltando ao menu...")
                    sleep(2)
                    self.ExibirMenu_Usuario() 
            else: 
                print("Erro! Opção inválida!")

    def LivrosCadastrados(self):
        print("\n| Livros Cadastrados |\n")
        for i, livro in enumerate(self.livros):
            print(f"LIVRO {i+1}:")
            livro.MostrarInfo()

    def MostrarLivros(self):
        if len(self.livros) == 0:
                print("\nNenhum livro encontrado!\n")
        for i, livro in enumerate(self.livros):
                print(f"LIVRO {i+1}:")
                livro.MostrarInfo()
        self.VoltarAoMenu()

    def CadastrarLivros(self):
        while True:
            try:
                quantidade = int(input("Digite a quantidade de livros que você gostaria de cadastrar: \n"))

                while quantidade < 1:
                    print("Erro! É impossível cadastrar um número negativo de livros!")
                    quantidade = int(input("Digite a novamente quantidade de livros que você gostaria de cadastrar: "))
                    continue
                break
            except ValueError:
                print("Erro! Você deve digitar números inteiros! ")

        for i in range(quantidade):
            try:
                titulo = input("\n| Digite o título do livro: ").title()
                autor = input("| Digite o nome do autor: ").title()
                ano = int(input("| Digite o ano de lançamento: "))

            except ValueError:
                print("Erro! O ano de lançamento deverá ser conter apenas números inteiros! Ex.: 2000\n")
                
            MeuLivro = Livro(autor, titulo, ano)
            self.livros.append(MeuLivro)

        self.LivrosCadastrados() 

        mais_livros = input("\nGostaria de cadastrar mais livros?\nS - para sim | M - para voltar ao menu\n").upper()
        if mais_livros == 'M':
            print("\nVoltando ao menu...")
            sleep(2)
            self.ExibirMenu_Funcionario()
        elif mais_livros == 'S':
            self.CadastrarLivros()
        else:
            print("Opção inválida!")
        self.salvar_dados()

    def RemoverLivro(self):
        if len(self.livros) == 0:
            print("\nNão há Nenhum livro para remover!\n")
            menu = input("Gostaria de voltar ao menu?\nS - para sim | N - para não\n").upper()
            if menu == 'N':
                exit()
            elif menu == 'S':
                self.ExibirMenu_Funcionario()
            else:
                print("Opção inválida!") 
        for i, livro in enumerate(self.livros):
            print(f"LIVRO {i+1}:")
            livro.MostrarInfo()
        remover = input("Digite o título de livro que você gostaria de remover: \n").title()
    
        encontrado = False
        for livro in self.livros:
            if remover == livro.titulo:
                self.livros.remove(livro)
                print(f"\nLivro {remover} removido da lista. ")
                encontrado = True
                break
      
        if not encontrado:        
            print("Livro não encontrado!")

            self.LivrosCadastrados()
            mais_livros = input("\nGostaria de remover mais um livro?\nS - para sim | M - para voltar ao menu\n").upper()
            if mais_livros == 'M':
                print("\nVoltando ao menu...")
                sleep(2)
                self.ExibirMenu()
            elif mais_livros == 'S':
                self.RemoverLivro()
            else:
                print("Opção inválida!")   
        self.salvar_dados()
                     
    def BuscarLivro(self):
        if len(self.livros) == 0:
                print("\nNenhum livro cadastrado na biblioteca!\n")
                menu = input("Gostaria de voltar ao menu?\nS - para sim | N - para não\n").upper()
                self.VoltarAoMenu()
        while True:
            busca_titulo = input("Busque por um título de livro: \n").title()
            encontrado = False
            
            for livro in self.livros:
                if livro.titulo == busca_titulo:
                    sleep(2)
                    print("Busca encontrada!\n")          
                    
                    livro.MostrarInfo()
                    self.VoltarAoMenu()
                    encontrado = True

            if not encontrado:
                sleep(2)
                print("Busca não encontrada!\n") 
            self.VoltarAoMenu()
    
    def BuscarLivros_Usuario(self):
        if len(self.livros) == 0:
                print("\nNenhum livro encontrado!\n")
                self.VoltarAoMenu()
        while True:
            busca_titulo = input("Busque por um título de livro: \n").title()
            encontrado = False
            
            for livro in self.livros:
                if livro.titulo == busca_titulo:
                    print("Buscando pesquisa...")
                    sleep(2)
                    print("Busca encontrada!\n")          
                    
                    livro.MostrarInfo()
                    encontrado = True

                    adicionar = input(f"Gostaria de adicionar o livro '{livro.titulo}' à sua biblioteca?\nS - para sim | N - para não\n").title()
                    if adicionar == 'N':
                        pass
                    elif adicionar == 'S':
                        print(f"Livro {livro.titulo} adicionado à sua biblioteca!")
                        self.biblioteca.append(livro)
                    else:
                        print("Opção inválida!\n")

            if not encontrado:
                sleep(2)
                print("Busca não encontrada!\n") 

            mais_livros = input("\nGostaria de buscar mais um livro?\nS - para sim | M - para voltar ao menu\n").upper()
            if mais_livros == 'M':
                print("\nVoltando ao menu...")
                sleep(2)
                if self.tipo == 1:
                    self.ExibirMenu_Usuario()
                elif self.tipo == 2:
                    self.ExibirMenu_Funcionario()
            elif mais_livros == 'S':
                self.BuscarLivro()
            else:
                print("Opção inválida!")
    
    def ExibirMinhaBiblioteca_Usuario(self):
        if len(self.biblioteca) == 0:
            print(f"\nSua biblioteca está vazia!\n")
            self.VoltarAoMenu()
        else:
            print(f"Você possui {len(self.biblioteca)} livro(s) em sua biblioteca\n")
            for i, livro in enumerate(self.biblioteca):
                print(f"LIVRO {i+1}:")
                livro.MostrarInfo()
                remover = input("Gostaria de remover algum livro de sua biblioteca?\nS - para sim | N - para não\n").title()
                if remover == 'N':
                    pass
                elif remover == 'S':
                    livro_remover = input("Qual o título do livro que você gostaria de remover? \n").title()
                    encontrado = False
                    
                    for livro in self.biblioteca:
                        if livro_remover == livro.titulo:
                            print(f"Livro {livro.titulo} removido da biblioteca.\n")
                            self.biblioteca.remove(livro)
                            encontrado = True
                    
                    if not encontrado:
                        print("Livro não encontrado.\n")
                
                else:
                    print("Opção inválida!\n")

            self.VoltarAoMenu()

    def AvaliarLivro(self):
        if len(self.biblioteca) == 0:
            print("Sua biblioteca está vazia! Adicione livros para avaliá-los!\n")
            self.VoltarAoMenu()    
        else:
            print("\nLivros Cadastrados: \n")
            for livro in self.biblioteca:
                livro.MostrarInfo()
                avaliar = input("Digite o título do livro que você gostaria de avaliar: \n").title()
                encontrado = False

                for livro in self.biblioteca:
                    if avaliar != livro.titulo:
                        print("Livro não encontrado!")
                    else:
                        try:
                            livro.avaliacao = int(input("Quantas estrelas você gostaria de atribuir a essa obra? 0 - 5\n"))
                            if livro.avaliacao < 0 or livro.avaliacao > 5:
                                print("O número deve ser entre 0 e 5!")
                            else:
                                print(f"Avaliação atribuída! {livro.avaliacao} estrelas para o livro '{livro.titulo}'\n")
                            encontrado = True
                        except ValueError:
                            print("Erro! A avaliação deverá ser feita através de números inteiros! \n")
        self.salvar_dados()
    
    def VoltarAoMenu(self):
        menu = input("Gostaria de voltar ao menu?\nS - para sim | N - para não\n").upper()
        if menu == 'S':
            if self.tipo == 1:
                print("Voltando ao menu...")
                sleep(2)
                self.ExibirMenu_Usuario()
            elif self.tipo == 2:
                print("Voltando ao menu...")
                sleep(2)
                self.ExibirMenu_Funcionario()
            elif menu == 'N':
                print("Saindo...")
                sleep(2)
                exit()
            else:
                print("Opção inválida!")
                exit()
   
if __name__ == '__main__':

    usuarios = []
    MinhaBiblioteca = Biblioteca()

    MinhaBiblioteca.TelaInicio()

