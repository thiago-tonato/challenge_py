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


# Função para editar um carro
def editar_carro():
    print("")
    placa = input("Digite a placa do carro que deseja editar: ").strip().upper()

    if placa in carros:
        novo_modelo = input("Digite o novo modelo do carro: ").strip()
        if novo_modelo:
            carros[placa]["modelo"] = novo_modelo
            print(f"Modelo do carro de placa {placa} atualizado para {novo_modelo}.")
        else:
            print("Modelo não pode ser vazio!")
    else:
        print(f"Carro com placa {placa} não encontrado.")


# Função para excluir um carro
def excluir_carro():
    print("")
    placa = input("Digite a placa do carro que deseja excluir: ").strip().upper()

    if placa in carros:
        del carros[placa]
        print(f"Carro de placa {placa} excluído com sucesso.")
    else:
        print(f"Carro com placa {placa} não encontrado.")


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


# Função para editar um problema de um carro existente
def editar_problema():
    print("")
    placa = input("Digite a placa do carro: ").strip().upper()

    if placa in carros:
        if carros[placa]["problemas"]:
            print(f"Problemas do carro {carros[placa]['modelo']}:")
            for i, problema in enumerate(carros[placa]["problemas"], 1):
                print(f"{i}. {problema}")

            try:
                indice = int(input("Digite o número do problema que deseja editar: ")) - 1
                if 0 <= indice < len(carros[placa]["problemas"]):
                    novo_problema = input("Digite o novo problema: ").strip()
                    if novo_problema:
                        carros[placa]["problemas"][indice] = novo_problema
                        print("Problema atualizado com sucesso.")
                    else:
                        print("O problema não pode ser vazio.")
                else:
                    print("Problema inválido.")
            except ValueError:
                print("Entrada inválida!")
        else:
            print("Não há problemas registrados para esse carro.")
    else:
        print(f"Carro com placa {placa} não encontrado.")


# Função para excluir um problema de um carro existente
def excluir_problema():
    print("")
    placa = input("Digite a placa do carro: ").strip().upper()

    if placa in carros:
        if carros[placa]["problemas"]:
            print(f"Problemas do carro {carros[placa]['modelo']}:")
            for i, problema in enumerate(carros[placa]["problemas"], 1):
                print(f"{i}. {problema}")

            try:
                indice = int(input("Digite o número do problema que deseja excluir: ")) - 1
                if 0 <= indice < len(carros[placa]["problemas"]):
                    carros[placa]["problemas"].pop(indice)
                    print("Problema excluído com sucesso.")
                else:
                    print("Problema inválido.")
            except ValueError:
                print("Entrada inválida!")
        else:
            print("Não há problemas registrados para esse carro.")
    else:
        print(f"Carro com placa {placa} não encontrado.")


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


# Função para editar uma data de manutenção existente
def editar_data_manutencao():
    print("")
    placa = input("Digite a placa do carro: ").strip().upper()

    if placa in carros:
        if carros[placa]["manutencoes"]:
            print(f"Manutenções registradas para o carro {carros[placa]['modelo']}:")
            for i, manutencao in enumerate(carros[placa]["manutencoes"], 1):
                print(f"{i}. {manutencao}")

            try:
                indice = int(input("Digite o número da manutenção que deseja editar: ")) - 1
                if 0 <= indice < len(carros[placa]["manutencoes"]):
                    nova_data = input("Digite a nova data da manutenção (dd/MM/yyyy): ").strip()
                    try:
                        nova_data_formatada = datetime.strptime(nova_data, "%d/%m/%Y").strftime("%d/%m/%Y")
                        carros[placa]["manutencoes"][indice] = nova_data_formatada
                        print("Data de manutenção atualizada com sucesso.")
                    except ValueError:
                        print("Data inválida! Digite no formato dd/MM/yyyy.")
                else:
                    print("Manutenção inválida.")
            except ValueError:
                print("Entrada inválida!")
        else:
            print("Não há manutenções registradas para esse carro.")
    else:
        print(f"Carro com placa {placa} não encontrado.")


# Função para excluir uma data de manutenção existente
def excluir_data_manutencao():
    print("")
    placa = input("Digite a placa do carro: ").strip().upper()

    if placa in carros:
        if carros[placa]["manutencoes"]:
            print(f"Manutenções registradas para o carro {carros[placa]['modelo']}:")
            for i, manutencao in enumerate(carros[placa]["manutencoes"], 1):
                print(f"{i}. {manutencao}")

            try:
                indice = int(input("Digite o número da manutenção que deseja excluir: ")) - 1
                if 0 <= indice < len(carros[placa]["manutencoes"]):
                    carros[placa]["manutencoes"].pop(indice)
                    print("Manutenção excluída com sucesso.")
                else:
                    print("Manutenção inválida.")
            except ValueError:
                print("Entrada inválida!")
        else:
            print("Não há manutenções registradas para esse carro.")
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
                        print("1. Gerenciar carros")
                        print("2. Gerenciar problemas")
                        print("3. Prever manutenção")
                        print("4. Gerenciar manutenções")
                        print("5. Histórico de manutenção")
                        print("6. Sair")

                        opcao_menu = input("Digite o número da opção que deseja: ")

                        match opcao_menu:
                            case "1":
                                while True:
                                    print("\nGerenciamento de Carros")
                                    print("-----------------------")
                                    print("1. Adicionar carro")
                                    print("2. Editar carro")
                                    print("3. Excluir carro")
                                    print("4. Voltar")
                                    opcao_carro = input("Digite a opção desejada: ")

                                    match opcao_carro:
                                        case "1":
                                            adicionar_carro()

                                        case "2":
                                            editar_carro()

                                        case "3":
                                            excluir_carro()

                                        case "4":
                                            break

                                        case _:
                                            print("Opção inválida!")

                            case "2":
                                while True:
                                    print("\nGerenciamento de Problemas")
                                    print("--------------------------")
                                    print("1. Adicionar problema")
                                    print("2. Editar problema")
                                    print("3. Excluir problema")
                                    print("4. Voltar")
                                    opcao_problema = input("Digite a opção desejada: ")

                                    match opcao_problema:
                                        case "1":
                                            adicionar_problema()

                                        case "2":
                                            editar_problema()

                                        case "3":
                                            excluir_problema()

                                        case "4":
                                            break

                                        case _:
                                            print("Opção inválida!")

                            case "3":
                                prever_manutencao()

                            case "4":
                                while True:
                                    print("\nGerenciamento de Manutenções")
                                    print("-----------------------------")
                                    print("1. Adicionar manutenção")
                                    print("2. Editar manutenção")
                                    print("3. Excluir manutenção")
                                    print("4. Voltar")
                                    opcao_manutencao = input("Digite a opção desejada: ")

                                    match opcao_manutencao:
                                        case "1":
                                            adicionar_data_manutencao()

                                        case "2":
                                            editar_data_manutencao()

                                        case "3":
                                            excluir_data_manutencao()

                                        case "4":
                                            break

                                        case _:
                                            print("Opção inválida!")

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
