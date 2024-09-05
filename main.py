import re  # Importa a biblioteca de expressões regulares para validação
import getpass  # Importa para ocultar a senha durante o cadastro/login
from datetime import datetime  # Importa para manipulação de datas

# Dicionário para armazenar os usuários cadastrados (login e senha)
usuarios = {}

# Dicionário para armazenar os carros cadastrados (placa, modelo, problemas e manutenções)
carros = {}


# Função para cadastrar um novo usuário
def cadastrar_usuario():
    while True:
        login = input("Digite seu login para cadastro: ").strip()
        if not login:  # Verifica se o login está vazio
            print("Login não pode ser vazio!")
            continue
        senha = getpass.getpass("Digite sua senha para cadastro: ").strip()
        if not senha:  # Verifica se a senha está vazia
            print("Senha não pode ser vazia!")
            continue
        usuarios[login] = senha  # Armazena o login e senha no dicionário de usuários
        print("\nCadastro realizado!")
        return True  # Retorna True para indicar sucesso no cadastro


# Função para realizar o login do usuário
def login_usuario():
    while True:
        nome_login = input("Digite seu login: ").strip()
        if not nome_login:  # Verifica se o login está vazio
            print("Login não pode ser vazio!")
            continue
        senha_login = getpass.getpass("Digite sua senha: ").strip()
        if not senha_login:  # Verifica se a senha está vazia
            print("Senha não pode ser vazia!")
            continue

        # Verifica se o login e senha são válidos
        if nome_login in usuarios and usuarios[nome_login] == senha_login:
            print("\nLogin realizado com sucesso!")
            return True  # Retorna True para indicar sucesso no login
        else:
            print("Login ou senha inválidos!")
            return False  # Retorna False para indicar falha no login


# Função para adicionar um carro ao sistema
def adicionar_carro():
    print("")
    placa = input("Digite a placa do carro (ex: ABC-1234): ").strip().upper()

    # Valida se a placa está no formato correto
    if not re.match(r"^[A-Z]{3}-\d{4}$", placa):
        print("Placa inválida! Use o formato ABC-1234.")
        return

    if placa in carros:  # Verifica se o carro já foi cadastrado
        print(f"O carro com placa {placa} já está cadastrado.")
    else:
        modelo = input("Digite o modelo do carro: ").strip()
        if modelo:  # Verifica se o modelo não está vazio
            # Adiciona o carro ao dicionário de carros
            carros[placa] = {"modelo": modelo, "problemas": [], "manutencoes": []}
            print(f"Carro {modelo} com placa {placa} adicionado com sucesso!")
        else:
            print("Modelo do carro não pode ser vazio.")


# Função para adicionar um problema a um carro existente
def adicionar_problema():
    print("")
    placa = input("Digite a placa do carro (ex: ABC-1234): ").strip().upper()

    if placa in carros:  # Verifica se o carro já está cadastrado
        problema = input(f"Digite o problema encontrado no carro {carros[placa]['modelo']}: ").strip()
        if problema:  # Verifica se o problema não está vazio
            # Adiciona o problema à lista de problemas do carro
            carros[placa]["problemas"].append(problema)
            print(f"Problema '{problema}' adicionado ao carro {carros[placa]['modelo']} de placa {placa}.")
        else:
            print("O problema não pode ser vazio.")
    else:
        print(f"Carro com placa {placa} não encontrado. Por favor, adicione o carro primeiro.")


# Função para prever a necessidade de manutenção com base nos problemas do carro
def prever_manutencao():
    print("")
    placa = input("Digite a placa do carro (ex: ABC-1234): ").strip().upper()

    if placa in carros:  # Verifica se o carro já está cadastrado
        if carros[placa]["problemas"]:  # Verifica se há problemas registrados no carro
            print(f"Manutenção recomendada para o carro {carros[placa]['modelo']} de placa {placa}.")
        else:
            print(f"Carro {carros[placa]['modelo']} de placa {placa} está em boas condições.")
    else:
        print(f"Carro com placa {placa} não encontrado.")


# Função para adicionar a data de uma manutenção ao histórico do carro
def adicionar_data_manutencao():
    print("")
    placa = input("Digite a placa do carro (ex: ABC-1234): ").strip().upper()

    if placa in carros:  # Verifica se o carro já está cadastrado
        while True:
            manutencao = input("Digite a data da manutenção (dd/MM/yyyy): ").strip()
            try:
                # Tenta converter a data inserida para o formato correto
                data_manutencao = datetime.strptime(manutencao, "%d/%m/%Y")
                data_formatada = data_manutencao.strftime("%d/%m/%Y")
                # Adiciona a data de manutenção ao histórico do carro
                carros[placa]["manutencoes"].append(data_formatada)
                print(f"Data de manutenção {data_formatada} adicionada ao carro de placa {placa} com sucesso!")
                break
            except ValueError:  # Captura o erro caso o formato da data seja inválido
                print("Data inválida! Digite a data no formato dd/MM/yyyy.")
    else:
        print(f"Carro com placa {placa} não encontrado. Por favor, adicione o carro primeiro.")


# Função para visualizar o histórico de manutenções de um carro
def visualizar_historico_manutencao():
    print("")
    placa = input("Digite a placa do carro (ex: ABC-1234): ").strip().upper()

    if placa in carros:  # Verifica se o carro já está cadastrado
        if carros[placa]["manutencoes"]:  # Verifica se o carro possui manutenções registradas
            print(f"Histórico de manutenções do carro {carros[placa]['modelo']} de placa {placa}:")
            for manutencao in carros[placa]["manutencoes"]:
                print(f"- {manutencao}")
        else:
            print(f"Não há manutenções registradas para o carro {carros[placa]['modelo']} de placa {placa}.")
    else:
        print(f"Carro com placa {placa} não encontrado.")


# Variável para rastrear se o usuário fez cadastro
cadastro = False

# Menu principal com repetição
while True:
    print("\n>>>CHEVOTECH<<<")
    print("---------------")
    print("1. Fazer Cadastro")
    print("2. Fazer login")
    print("3. Sair")
    print("---------------")

    try:
        opcao_login = int(input("Digite o número da opção que deseja: "))
    except ValueError:
        print("Opção inválida! Digite um número.")
        continue

    match opcao_login:
        case 1:
            # Realizar cadastro de novo usuário
            cadastro = cadastrar_usuario()

        case 2:
            # Realizar login
            if cadastro:  # Verifica se o cadastro já foi feito
                if login_usuario():
                    # Menu principal após o login
                    while True:
                        print("\n>>>CHEVOTECH<<<")
                        print("---------------")
                        print("1. Adicionar carro")
                        print("2. Adicionar problema ao carro")
                        print("3. Prever manutenção")
                        print("4. Adicionar data da manutenção")
                        print("5. Histórico de manutenção")
                        print("6. Sair")

                        opcao_menu = input("Digite o número da opção que deseja: ")

                        match opcao_menu:
                            case "1":
                                adicionar_carro()

                            case "2":
                                adicionar_problema()

                            case "3":
                                prever_manutencao()

                            case "4":
                                adicionar_data_manutencao()

                            case "5":
                                visualizar_historico_manutencao()

                            case "6":
                                # Logout e sair do menu
                                print("\nLogOut feito! Obrigado!")
                                break

                            case _:
                                print("Digite uma opção válida!")
                else:
                    print("Login ou senha inválidos!")
            else:
                print("Realize o cadastro para fazer login!")

        case 3:
            # Encerrar o programa
            print("Obrigado!")
            break

        case _:
            # Opção inválida no menu principal
            print("Opção inválida")
