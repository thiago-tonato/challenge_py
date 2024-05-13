# Importando as bibliotecas necessárias para o funcionamento do código
import numpy as np
import getpass
from datetime import datetime

# Dicionário para armazenar os usuários e senhas cadastrados
usuarios = {}
# Lista para armazenar as datas das manutenções realizadas
lista_manutencoes = []
# Lista para armazenar os dados coletados pelos sensores
dados_sensores = []


# Função para cadastrar um novo usuário
def Cadastro():
    login = input("Digite seu login para cadastro: ")
    senha = getpass.getpass("Digite sua senha para cadastro: ")
    usuarios[login] = senha
    print("")
    print("Cadastro realizado!")
    return True


# Função para realizar o login do usuário
def Login():
    nome_login = input("Digite seu login: ")
    senha_login = getpass.getpass("Digite sua senha: ")
    if nome_login in usuarios and usuarios[nome_login] == senha_login:
        print("")
        print("Login realizado com sucesso!")
        return True
    else:
        return False


# Função para simular a coleta de dados dos sensores
def ColetarDados():
    dados_sensores.extend(np.random.rand(10))
    print("Dados coletados: ", dados_sensores)
    print("Dados dos sensores coletados com sucesso!")


# Função para prever a necessidade de manutenção com base nos dados coletados
def Prever():
    threshold = 0.45
    print("")
    if np.mean(dados_sensores) > threshold:
        print("Manutenção recomendada.")
    else:
        print("Nenhuma manutenção necessária!")


# Função para adicionar a data de uma manutenção à lista de manutenções
def AddDataManutencao():
    print("")
    while True:
        manutencao = input("Digite a data da manutenção (dd/MM/yyyy): ")
        try:
            data_manutencao = datetime.strptime(manutencao, "%d/%m/%Y")
            data_formatada = data_manutencao.strftime("%d/%m/%Y")
            lista_manutencoes.append(data_formatada)
            print(f"Data de manutenção {data_formatada} adicionada com sucesso!")
            break
        except ValueError:
            print("Data inválida! Digite a data no formato dd/MM/yyyy.")


cadastro = False
# Menu com repetição para login
while True:
    print("")
    print(">>>CHEVOTECH<<<")
    print("---------------")
    print("1. Fazer Cadastro")
    print("2. Fazer login")
    print("3. Sair")
    print("---------------")

    opcao_login = int(input("Digite o número da opção que deseja: "))

    match opcao_login:
        case 1:
            # Cadastrar
            cadastro = Cadastro()
        case 2:
            # Login
            if cadastro:
                if Login():
                    print("")
                    print(">>>CHEVOTECH<<<")
                    print("---------------")
                    # Menu principal do programa
                    while True:
                        print("")
                        print(">>>CHEVOTECH<<<")
                        print("---------------")
                        print("Bem vindo! O que deseja fazer?")
                        print("")
                        print("1. Coletar dados dos sensores")
                        print("2. Prever manutenção")
                        print("3. Adicionar data da manutenção")
                        print("4. Histórico de manutenção")
                        print("5. Sair")

                        opcao_menu = input("Digite o número da opção que deseja: ")

                        match opcao_menu:
                            case "1":
                                # Chamando função para coletar dados dos sensores
                                ColetarDados()
                            case "2":
                                # Chamando função para prever a necessidade de manutenção
                                Prever()
                            case "3":
                                # Chamando função para adicionar a data de uma manutenção
                                AddDataManutencao()
                            case "4":
                                # Mostrando o histórico de manutenções realizadas
                                print("")
                                print(f"Manutenções feitas nos dias: {lista_manutencoes}")
                            case "5":
                                # Finalizando a sessão e saindo do programa
                                print("")
                                print("LogOut feito! Obrigado!")
                                break
                            case _:
                                # Caso não seja nenhum dos casos anteriores
                                print("")
                                print("Digite uma opção válida!")
                else:
                    # Se usuário ou senha estiverem incorretos
                    print("")
                    print("Login ou senha inválidos!")
            else:
                # Se o usuário tentar fazer login sem ter feito cadastro
                print("")
                print("Realize o cadastro para fazer login!")
        case 3:
            # Sair do programa
            print("")
            print("Obrigado!")
            break
        case _:
            # Caso o usuário digite uma opção inválida
            print("Opção inválida")
